
function save_and_quit()
        add_timer(30,function()
            print("<<<<<<<<<<<<<<<<<< SAVE")
            send("save")
            add_timer(3,function()
                        print("<<<<<<<<<<<<<<<<<< QUIT")
                        send("quit")
            end,uuid())
        end,uuid())
    end


add_alias("lg", function(p)
    local id1=uuid()
    local id2=uuid()
    local id3=uuid()
    local id4=uuid()

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
    print(">>>>>>> dazuo 20")
    send("dazuo 20")
    
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id1)
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
    end,uuid())
    
    addtrigger(id1,
    "你运功完毕，深深吸了口气，站了起来。",
    function()
        print(">>>>>>> dazuo 20")
        send("dazuo 20")
    end)
    
    addtrigger(id2,
    "你现在的气太少了，无法产生内息运行全身经脉。",
    function()
        print(">>>>>>> sleep")
        send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        print(">>>>>>> dazuo 20")
        send("dazuo 20")

    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        print("<<<<<<<<<<<<<<<<<< do 4 w")
        send("do 4 w")
        add_timer(3,function()
            print("<<<<<<<<<<<<<<<<<<<<<< get all")
            send("get all")
            add_timer(3,function()
                print("<<<<<<<<<< do 4 e")
                send("do 4 e")
                add_timer(3,function()
                    print("<<<<<<<<<<<<<<<<<< sleep")
                    send("sleep")
                end,uuid())
            end,uuid())
        end,uuid())
    end)
        
end)

add_alias("sj", function(p)

    print("<<<<<<<<<<<<<<<<<< sleep")
    send("sleep")
    local wake_id=uuid()
    addtrigger(wake_id,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake"..wake_id)
    end)

end)

add_alias("xx", function(p)
    local id2=uuid()
    local id3=uuid()
    local id4=uuid()

    local parameters={}
    parameters[1],parameters[2]=p[-1]:match("(%w+)(.+)")

   local time_lenth=parameters[1] or 60
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
   local topic=parameters[2] or "begging"

   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
   print(">><<<<<<<<<<<<<<<<<<<<<<<<<< topic "..topic)

    function worker()
        print(">>>>>>> xue "..topic)
        send("xue qiu for"..topic.." 50")
    end
    
    worker()

    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
    end,uuid())
    
    addtrigger(id2,
    "你今天太累了，结果什么也没有学到。",
    function()
        print(">>>>>>> sleep")
        send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        worker()
    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        send("get all")
        add_timer(10,function()
                    print("<<<<<<<<<<<<<<<<<< sleep again")
                    send("sleep")
        end,uuid())
    end)
        
end)

add_alias("xxq", function(p)
    local id2=uuid()
    local id3=uuid()
    local id4=uuid()

    local parameters={}
    parameters[1],parameters[2]=p[-1]:match("(%w+)(.+)")

   local time_lenth=parameters[1] or 60
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
   local topic=parameters[2] or "begging"

   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
   print(">><<<<<<<<<<<<<<<<<<<<<<<<<< topic "..topic)

    function worker()
        print(">>>>>>> xue "..topic)
        send("xue qiu for"..topic.." 50")
    end
    
    worker()

    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
        save_and_quit()
    end,uuid())
    
    addtrigger(id2,
    "你今天太累了，结果什么也没有学到。",
    function()
        print(">>>>>>> sleep")
        send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        worker()
    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        send("get all")
        send("cha")
        send("hp")
        add_timer(10,function()
                    print("<<<<<<<<<<<<<<<<<< sleep again")
                    send("sleep")
        end,uuid())
    end)
        
end)

add_alias("lgq", function(p)
    local id1=uuid()
    local id2=uuid()
    local id3=uuid()
    local id4=uuid()

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
    print(">>>>>>> dazuo 20")
    send("dazuo 20")
    
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id1)
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
        save_and_quit()
    end,uuid())
    
    addtrigger(id1,
    "你运功完毕，深深吸了口气，站了起来。",
    function()
        print(">>>>>>> dazuo 20")
        send("dazuo 20")
    end)
    
    addtrigger(id2,
    "你现在的气太少了，无法产生内息运行全身经脉。",
    function()
        print(">>>>>>> sleep")
        send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        print(">>>>>>> dazuo 20")
        send("dazuo 20")

    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        print("<<<<<<<<<<<<<<<<<< do 4 w")
        send("do 4 w")
        add_timer(3,function()
            print("<<<<<<<<<<<<<<<<<<<<<< get all")
            send("get all")
            add_timer(3,function()
                print("<<<<<<<<<< do 4 e")
                send("do 4 e")
                add_timer(3,function()
                    print("<<<<<<<<<<<<<<<<<< sleep")
                    send("sleep")
                end,uuid())
            end,uuid())
        end,uuid())
    end)
        
end)

