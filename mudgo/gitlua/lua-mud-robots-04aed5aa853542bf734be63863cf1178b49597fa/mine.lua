
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
        execs(";dazuo 20",10)
        -- print("<<<<<<<<<<<<<<<<<< do 4 w")
        -- send("do 4 w")
        -- add_timer(3,function()
        --     print("<<<<<<<<<<<<<<<<<<<<<< get all")
        --     send("get all")
        --     add_timer(3,function()
        --         print("<<<<<<<<<< do 4 e")
        --         send("do 4 e")
        --         add_timer(3,function()
        --             print("<<<<<<<<<<<<<<<<<< sleep")
        --             send("sleep")
        --         end,uuid())
        --     end,uuid())
        -- end,uuid())
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
    local id1="xx1"
    local id2="xx2"
    local id3="xx3"
    local id4="xx4"
    local id5="xx5"

    local parameters={}
    parameters[1],parameters[2]=p[-1]:match("(%w+)(.+)")

   local time_lenth=parameters[1] or 60
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
   local master=parameters[2] or "qiu"

   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
   print(">><<<<<<<<<<<<<<<<<<<<<<<<<< shifu "..master)
    
    local xx1=true
    local xx2=false
    local xx3=false
    local xx4=false
    local xx5=false

    local tlist={
'literate',
--     'blade',
--     'liuhe-dao',
--     'hand',
--     'dodge',
--     'force',
--     'parry',
--     'huntian-qigong',
    'xiaoyaoyou',
    'begging',
'nothing'}
    -- local master='qiu'
    local t_idx=1

    function xue_xi_worker(times)
            xx1=true
            xx2=true
            xx4=false
            xx3=false
            xx5=true
            times=times or 1
        if t_idx <= #tlist then
            print("<<<<<<<<<<<<<<<<<< xue "..tostring(t_idx)..":"..tlist[t_idx])
            send("xue"..master.." for "..tlist[t_idx].." "..tostring(times))
        else
            print("<<<<<<<<<<<<<<<<<< no more to learn.")
        end
    end

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
    
    addtrigger(id1,"^其中.*似乎有些心得。$",
    function()
        if xx1 then
            print("<<<<<<<<<<<<<<<<<< xue again.")
            xue_xi_worker(50)
        end
    end)

    addtrigger(id5,"^你.*(消耗了大量潜能|实战经验).*",
    function()
        if xx5 then
            print("<<<<<<<<<<<<<<<<<< xue next.")
            xx5=false
            t_idx=t_idx+1
            xue_xi_worker()
        end
    end)

    addtrigger(id2,
    "你今天太累了，结果什么也没有学到。",
    function()
        if xx2 then
            xx1=false
            xx2=false
            xx3=true
            xx4=true
            xx5=false
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
            xx1=true
            xx3=false
            xx2=false
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
            xx1=false
            xx2=false
            xx4=false
        -- close_trigger(id4)
        -- send("get all")
        execs("get all;hp;cha",3)
        add_timer(10,function()
            xx4=true
            xx3=true
            -- open_trigger(id4)
            -- open_trigger(id3)
            xue_xi_worker(50)
            -- print("<<<<<<<<<<<<<<<<<< sleep again")
            -- send("sleep")
        end,uuid())
    end
    end)
        
end)

