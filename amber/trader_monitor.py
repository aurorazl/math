from test_case import *

# 实现一个虚拟时间的TTL字典
class TTLCache:
    def __init__(self,ttl):
        self.ttl = ttl
        self.__DATA = {}
    def __getitem__(self, item):
        return self.__DATA[item]
    def __setitem__(self, key, value):
        self.__DATA[key]=value
    def items(self,time):
        tmp=[]
        for k,v in self.__DATA.items():
            if k == "alert":
                if v < time-self.ttl:
                    tmp.append(k)
            else:
                if k >= time-self.ttl:
                    yield k,v
                else:
                    tmp.append(k)
        for one in tmp:
            self.__DATA.pop(one)
    def __contains__(self, item):
        return True if item in self.__DATA else False

# 可以在此基础上进行任意的设计和修改
class TradeMonitor:
    def __init__(self):
        pass

    def find_symbol_or_group_or_exchange(self,name,atype):
        # 先查缓存
        if "membership_{}_{}".format(atype,name) in Global_Data:
            return Global_Data["membership_{}_{}".format(atype,name)]
        # 如果缓存没有，就根据name查找
        for one in Global_Data[atype]:
            if one.name == name:
                Global_Data["membership_{}_{}".format(atype,name)] = one
                return one
        # 不存在的情况，抛出异常
        raise Exception("not found {} in {}".format(name,atype))

    def on_trade(self, trade):
        # 找出所属的SYMBOL、GROUP、EXCHANGE
        THIS_SYMBOL = self.find_symbol_or_group_or_exchange(trade["name"],"symbols")
        THIS_GROUP = self.find_symbol_or_group_or_exchange(THIS_SYMBOL.group_name,"groups")
        THIS_EXCHANGE = self.find_symbol_or_group_or_exchange(THIS_SYMBOL.exchange_name,"exchanges")
        max_quantity_interval = max(THIS_SYMBOL.quantity_interval,THIS_EXCHANGE.quantity_interval,THIS_GROUP.quantity_interval)
        max_delta_interval = max(THIS_SYMBOL.delta_interval,THIS_EXCHANGE.delta_interval,THIS_GROUP.delta_interval)

        # 根据interval来生成缓存cache，quantity和delta分开，每个symbol维护自己的缓存
        Global_Data.setdefault("quantity", {})
        Global_Data.setdefault("delta", {})
        Global_Data["quantity"].setdefault(trade["name"],TTLCache(ttl=max_quantity_interval))
        Global_Data["delta"].setdefault(trade["name"],TTLCache(ttl=max_delta_interval))

        # 缓存当前交易
        if trade["time"] not in Global_Data["quantity"][trade["name"]]:
            Global_Data["quantity"][trade["name"]][trade["time"]] = [trade]
        else:
            Global_Data["quantity"][trade["name"]][trade["time"]].append(trade)
        if trade["time"] not in Global_Data["delta"][trade["name"]]:
            Global_Data["delta"][trade["name"]][trade["time"]] = [trade]
        else:
            Global_Data["delta"][trade["name"]][trade["time"]].append(trade)

        # 计算累计结果
        total_quantity = [0,0,0]
        total_delta = [0,0,0]
        ### 找出当前symbol同一exchange、group的全部symbols
        same_group_symbols = [i.name for i in Global_Data["symbols"] if i.group_name == THIS_GROUP.name]
        same_exchange_symbols = [i.name for i in Global_Data["symbols"] if i.exchange_name == THIS_EXCHANGE.name]

        ### 计算interval间隔内symbol、所在exchange、所在group的总quantity
        for symbol,symbol_ttl in Global_Data["quantity"].items():
            for trace_time, trace_info_list in symbol_ttl.items(trade["time"]):
                if symbol == THIS_SYMBOL.name and trade["time"]-trace_time<THIS_SYMBOL.quantity_interval:
                    if trace_time!="alert":
                        for trace_info in trace_info_list:
                            total_quantity[0]+=trace_info["quantity"]
                if symbol in same_exchange_symbols and trade["time"]-trace_time<THIS_EXCHANGE.quantity_interval:
                    if trace_time != "alert":
                        for trace_info in trace_info_list:
                            total_quantity[1]+=trace_info["quantity"]
                if symbol in same_group_symbols and trade["time"]-trace_time<THIS_GROUP.quantity_interval:
                    for trace_info in trace_info_list:
                        if trace_time != "alert":
                            total_quantity[2]+=trace_info["quantity"]

        ### 计算interval间隔内symbol、所在exchange、所在group的总delta
        for symbol,symbol_ttl in Global_Data["delta"].items():
            for trace_time, trace_info_list in symbol_ttl.items(trade["time"]):
                if symbol == THIS_SYMBOL.name and trade["time"]-trace_time<THIS_SYMBOL.quantity_interval:
                    if trace_time != "alert":
                        for trace_info in trace_info_list:
                            total_delta[0] += trace_info["quantity"] * trace_info["price"] * (1 if trace_info["side"] == "BUY" else -1)
                if symbol in same_exchange_symbols:
                    if trace_time != "alert" and trade["time"]-trace_time<THIS_EXCHANGE.quantity_interval:
                        for trace_info in trace_info_list:
                            total_delta[1] += trace_info["quantity"] * trace_info["price"] * (1 if trace_info["side"] == "BUY" else -1)
                if symbol in same_group_symbols and trade["time"]-trace_time<THIS_GROUP.quantity_interval:
                    if trace_time != "alert":
                        for trace_info in trace_info_list:
                            total_delta[2] += trace_info["quantity"] * trace_info["price"] * (1 if trace_info["side"] == "BUY" else -1)

        ### 对delta求对消后的绝对值
        for index in range(len(total_delta)):
            if total_delta[index]<0:
                total_delta[index] *= -1

        # 按照当前symbol、exchange、group的顺序报警
        alert_list = [(THIS_SYMBOL,[THIS_SYMBOL.name],"symbol"),(THIS_EXCHANGE,same_exchange_symbols,"exchange"),(THIS_GROUP,same_group_symbols,"group")]
        for index,(alert_item,symbol_list,asource) in enumerate(alert_list,0):
            if alert_item.quantity_limit <= total_quantity[index]:
                for one_symbol in symbol_list:
                    self.traggle_alert(one_symbol, "quantity",alert_item.quantity_limit,total_quantity[index],alert_item.name,trade["time"],asource)

            if alert_item.delta_limit <= total_delta[index]:
                for one_symbol in symbol_list:
                    self.traggle_alert(one_symbol, "delta",alert_item.delta_limit,total_delta[index],alert_item.name,trade["time"],asource)

        print("trace is {}, symbol\exchange\group's quantity is {},delta is {}".format(trade,total_quantity,total_delta))

    @staticmethod
    def traggle_alert(symbol_name,atype,threshold,current_value,asource,alert_time,source_type):
        if "alert" not in Global_Data[atype][symbol_name]:
            Global_Data[atype][symbol_name]["alert"] = alert_time
            msg = "reason: {} {} exceed limit threshold: {}  current: {} ".format(source_type,asource,threshold,current_value)
            TradeMonitor.alarm(alert_time, symbol_name, atype=atype,msg=msg)

    @staticmethod
    def alarm(atime, name, atype='quantity',msg=""):
        alarm_msg = '累计成交量报警'+msg
        if atype == 'delta':
            alarm_msg = '累计Delta报警'+msg
        print(atime, name, alarm_msg)


if __name__ == "__main__":
    monitor = TradeMonitor()

    load_param_data1()
    load_trade_data1(monitor)

    load_param_data2()
    load_trade_data2(monitor)
