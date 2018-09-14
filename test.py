#!/usr/bin/python
# -*- coding: UTF-8 -*-
import trackingmoreclass
tracker = trackingmoreclass.track
result = ""

#1 List all carriers(列出所有运输商)
#urlStr = ""
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "carriers")

#2 detect a carriers by tracking number(识别运输商)
#urlStr = ""
#requestData = "{\"tracking_number\":\"RS907483608CH\"}"
#result = tracker.trackingmore(requestData, urlStr, "carriers/detect")

#3 create a tracking number(新建一个单号)
#urlStr = ""
requestData = "{\"tracking_number\": \"RS907483608CH\",\"carrier_code\":\"swiss-post\",\"title\":\"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"order_create_time\":\"2018/09/08 16:51\",\"destination_code\":\"US\",\"tracking_ship_date\":\"20180908\",\"tracking_postal_code\":\"12201\",\"lang\":\"en\",\"logistics_channel\":\"API TEST\"}"
result = tracker.trackingmore(requestData, urlStr, "post")

#4 List all trackings(列出所有跟踪)
#urlStr = "?page=1&limit=100&created_at_min=&created_at_max=&update_time_min=&update_time_max=&order_created_time_min=&order_created_time_max=&numbers=RS907483608CH&orders=&lang=en"
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "get")

#5 Get tracking results of a single tracking.
#urlStr = "/swiss-post/RS907483608CH/en"
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "codeNumberGet")

#6 create muti tracking number(创建多个订单号)
#urlStr = ""
#requestData = "[{\"tracking_number\": \"RS907483608CH\",\"carrier_code\":\"swiss-post\",\"title\":\"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"order_create_time\":\"2018/09/08 16:51\",\"destination_code\":\"US\",\"tracking_ship_date\":\"20180908\",\"tracking_postal_code\":\"12201\",\"lang\":\"en\",\"logistics_channel\":\"API TEST\"},{\"tracking_number\": \"LZ448865302CN\",\"carrier_code\":\"china-ems\",\"title\":\"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"order_create_time\":\"2018/09/08 16:51\",\"destination_code\":\"US\",\"tracking_ship_date\":\"20180908\",\"tracking_postal_code\":\"12201\",\"lang\":\"en\",\"logistics_channel\":\"API TEST\"}]"
#result = tracker.trackingmore(requestData, urlStr, "batch")

#7 Update Tracking item(更新一个单号)
#urlStr = "/swiss-post/RS907483608CH"
#requestData = "{\"title\": \"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"logistics_channel\":\"API TEST\",\"customer_phone\":\"+86 13142052920\",\"destination_code\":\"US\",\"status\":\"7\"}"
#result = tracker.trackingmore(requestData, urlStr, "codeNumberPut")

#8 Delete a tracking item(删除一个单号)
#urlStr = "/swiss-post/RS907483608CH"
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "codeNumberDelete")

#9 Get realtime tracking results of a single tracking(获取单次跟踪的实时跟踪结果)
#urlStr = ""
#requestData = "{\"tracking_number\": \"RS907483608CH\",\"carrier_code\":\"swiss-post\",\"destination_code\":\"US\",\"tracking_ship_date\": \"20180908\",\"tracking_postal_code\":\"12201\",\"specialNumberDestination\":\"UK\",\"order\":\"#123\",\"order_create_time\":\"2018/09/08 16:51\",\"lang\":\"en\"}"
#result = tracker.trackingmore(requestData, urlStr, "realtime")

#10 Modify courier code(修改运输商)
#urlStr = ""
#requestData = "{\"tracking_number\": \"RS907483608CH\",\"carrier_code\":\"swiss-post\",\"update_carrier_code\":\"china-ems\"}"
#result = tracker.trackingmore(requestData, urlStr, "update")

#11 Get user info(获取个人信息)
#urlStr = ""
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "getuserinfo")

#12 Get status number(获取单号状态)
#urlStr = ""
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "getstatusnumber")

#13 Set number not update(设置单号不再更新)
#urlStr = ""
#requestData = "[{\"tracking_number\":\"RS907483608CH\",\"carrier_code\":\"swiss-post\"},{\"tracking_number\":\"LZ448865302CN\",\"carrier_code\":\"swiss-post\"}]"
#result = tracker.trackingmore(requestData, urlStr, "notupdate")

#14 Get remote iterm results(偏远)
#urlStr = ""
#requestData = "[{\"country\":\"CN\",\"postcode\":\"400422\"},{\"country\":\"CN\",\"postcode\":\"412000\"}]"
#result = tracker.trackingmore(requestData, urlStr, "remote")

#15 Get cost time iterm results(花费时间)
#urlStr = ""
#requestData = "[{\"carrier_code\":\"swiss-post\",\"destination\":\"US\",\"original\":\"CN\"},{\"carrier_code\":\"china-ems\",\"destination\":\"US\",\"original\":\"CN\"}]"
#result = tracker.trackingmore(requestData, urlStr, "costtime")

#16 Delete multiple tracking item(批量删除)
#urlStr = ""
#requestData = "[{\"tracking_number\":\"RS907483608CH\",\"carrier_code\":\"swiss-post\"},{\"tracking_number\":\"LZ448865302CN\",\"carrier_code\":\"china-ems\"}]"
#result = tracker.trackingmore(requestData, urlStr, "delete")

#17 Update multiple Tracking item
#urlStr = ""
#requestData = "[{\"tracking_number\":\"RS907483608CH\",\"carrier_code\":\"swiss-post\",\"title\": \"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"logistics_channel\":\"API TEST\",\"destination_code\":\"US\",\"status\":\"7\"},{\"tracking_number\":\"LZ448865302CN\",\"carrier_code\":\"china-ems\",\"title\": \"4PX page\",\"customer_name\":\"trackingmore user\",\"customer_email\":\"service@trackingmore.com\",\"order_id\":\"#123\",\"logistics_channel\":\"API TEST\",\"destination_code\":\"US\",\"status\":\"7\"}]"
#result = tracker.trackingmore(requestData, urlStr, "updatemore")



print(result)