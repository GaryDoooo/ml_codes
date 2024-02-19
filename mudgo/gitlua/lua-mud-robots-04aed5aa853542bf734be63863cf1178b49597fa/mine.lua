
function save_and_quit()
        add_timer(1,function()
            print("<<<<<<<<<<<<<<<<<< SAVE")
            send("save")
            add_timer(3,function()
                        print("<<<<<<<<<<<<<<<<<< QUIT")
                        send("quit")
            end,uuid())
        end,uuid())
    end

add_alias("wait_quit",function()
    print("<<<<<<<<<<<<<<<<<< wait_quit")
    addtrigger("wait_quit",
    "你跳了起来。",
    function()
        save_and_quit()
    end)
end)


add_alias("lg", function(p)
    local id1="lg1"
    local id2="lg2"
    local id3="lg3"
    local id4="lg4"

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
        add_timer(30,function()
            send("jump")
        end,uuid())
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

function xue_xi_worker()
    local function values(t)
            local i = 0
                return function() i = i + 1; return t[i] end
            end
    local tlist={ 'dodge','force','parry','huntian-qigong','xiaoyaoyou','begging'}
        -- blade                     │ 已有小成    │ 450.00      │ 485         │
        -- │   基本轻功                │ dodge                     │ 鹤立鸡群    │ 500.00      │ 485         │
        -- │   基本内功                │ force                     │ 已有小成    │ 450.00      │ 485         │
        -- │   基本手法                │ hand                      │ 已有小成    │ 450.00      │ 485         │
        -- │   基本招架                │ parry                     │ 略有小成    │ 430.00      │ 485         │
        -- ├───────四项特殊功夫────────┼───────────────────────────┼─────────────┼─────────────┼─────────────┤
        -- │ □ 混天气功                │ huntian-qigong            │ 鹤立鸡群    │ 500.00      │ 485         │
        -- │ □ 六合刀                  │ liuhe-dao                 │ 已有小成    │ 450.00      │ 485         │
        -- │ □ 蛇形手                  │ shexing-shou              │ 已有小成    │ 450.00      │ 485         │
        -- │ □ 逍遥游                  │ xiaoyaoyou
    -- print(">>>>>>> xue "..topic)
   for topic1 in values(tlist) do
        send("xue qiu for "..topic1.." 50")
    end
end

add_alias("xx", function(p)
    local id2="xx2"
    local id3="xx3"
    local id4="xx4"

    local parameters={}
    parameters[1],parameters[2]=p[-1]:match("(%w+)(.+)")

   local time_lenth=parameters[1] or 60
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
   local topic=parameters[2] or "begging"

   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
   print(">><<<<<<<<<<<<<<<<<<<<<<<<<< topic "..topic)

    local xx2=true
    local xx3=true
    local xx4=true

    xue_xi_worker()

    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        -- send("jump")
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
        add_timer(30,function()
            send("jump")
        end,uuid())
    end,uuid())
    
    addtrigger(id2,
    "你今天太累了，结果什么也没有学到。",
    function()
        if xx2 then
            xx2=false
            xx3=true
            xx4=true
        -- close_trigger(id2)
        -- open_trigger(id3)
        -- open_trigger(id4)
        print(">>>>>>> sleep")
        send("sleep");
    end
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        if xx3 then
            xx3=false
            xx2=true
            xx4=false
        -- close_trigger(id3)
        -- open_trigger(id2)
        -- close_trigger(id4)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        xue_xi_worker()
    end
    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        if xx4 then
            xx4=false
        -- close_trigger(id4)
        send("get all")
        add_timer(10,function()
            xx4=true
            xx3=true
            -- open_trigger(id4)
            -- open_trigger(id3)
            print("<<<<<<<<<<<<<<<<<< sleep again")
            send("sleep")
        end,uuid())
    end
    end)
        
end)

