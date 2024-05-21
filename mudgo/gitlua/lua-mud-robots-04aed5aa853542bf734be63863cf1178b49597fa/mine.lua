
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
    local id5="lg5"
    local cnt=0

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
    print(">>>>>>> dazuo 600")
    send("dazuo 600")
    
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id1)
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
        deltrigger(id5)
        execs("jump;jump;jump;jump",20)
    end,uuid())
    
    addtrigger(id1,
    "你运功完毕，深深吸了口气，站了起来。",
    function()
        print(">>>>>>> dazuo ")
        send("dazuo 20")
    end)
    
    addtrigger(id2,
    "你现在的气太少了，无法产生内息运行全身经脉。",
    function()
        print(">>>>>>> sleep")
        cnt=cnt+1
        if cnt%30==0 then
            send("save")
        end
        execs(";drink;eat mantou;sleep",1)
        -- send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        print(">>>>>>> dazuo 600")
        send("dazuo 600")

    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        execs("drink;eat mantou;dazuo 20",5)
    end)

    addtrigger(id5,"^你现在精不够.*",function()
        execs("yun regenerate;dazuo 20",1)
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
    local food=myvar["food"]
    local lian=myvar["lian"]

    local tlist={
-- 'literate',
--     'blade',
--     'liuhe-dao',
--     'hand',
--     'dodge',
--     'force',
--     'parry',
    'huntian-qigong',
    -- 'xiaoyaoyou',
    -- 'begging',
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
        execs("eat "..food..";drink;yun regenerate",3)
        add_timer(10,function()
            xx4=true
            xx3=true
            xue_xi_worker(50)
        end,uuid())
    end
    end)
        
end)


add_alias("shediao", function(p)
    local id1="xx1"
    local id2="xx2"
    local id3="xx3"
    local id4="xx4"
    local id5="xx5"

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
    
    local dushu=true
    local yungong=false
    local shuijiao=false
    local time_out=false

    local book=myvar["book"]
    local food=myvar["food"]
    local lian=myvar["lian"]
    -- local xuecmd=myvar["xuecmd"]

    book=book or "shediao"
    food=food or "mantou"
    lian=lian or "dodge"

    function dushu_worker()
        if time_out then
            return
        end
        if dushu then
            dushu=false
            yungong=true
            shuijiao=false
            --------------
            watch_dog=false
            if book=="shediao" then
                execs("read "..book.." 50")
            else 
                if book=="table" then
                    execs("do 10 study table;do 10 study table",1)
                else
                    execs("du "..book.." for 50")
                end
            end
        end
    end

    function shuijiao_worker()
        if time_out then
            return
        end
        dushu=false
        yungong=false
        shuijiao=false
        --------------
        watch_dog=false
        execs("drink;eat "..food..";lian "..lian.." 50;lian "..lian.." 50;sleep",1)
    end


    local watch_dog=true
    local watch_dog_cnt=0

    function watch_dog_reset()
        if time_out then
            return
        end
        watch_dog_cnt=watch_dog_cnt+1
        if watch_dog_cnt % 10 == 0 then
            send("save")
        end
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< watch_dog reset.")
        watch_dog=true
        add_timer(60,function()
            if watch_dog then
                dushu=true
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< watch_dog triggered")
                dushu_worker()
            end
            watch_dog_reset()
        end,"shediao_watchdog")
    end

    watch_dog_reset()
    dushu_worker()
    
    add_timer(time_lenth,function()
        time_out=true
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id2)
        deltrigger(id1)
        deltrigger(id3)
        if myvar["quit"]=="yes" then
            execs(";;;;;save;quit",10)
        else
            execs("jump;jump;jump;jump;jump;jump;save",10)
        end
    end,"shediao_timeout")
    
    addtrigger(id1,"^(你今天太累了|你已经很累了|你现在过于疲倦).*",--，无法专心下来研读新知。
    function()
        if time_out then
            return
        end
        if yungong then
            yungong=false
            dushu=true
            shuijiao=true
            print("<<<<<<<<<<<<<<<<<<  yungong.")
            add_timer(3, function()
                if shuijiao then
                    shuijiao_worker()
                end
            end,uuid())
            watch_dog=false
            execs("yun regenerate")
        end
    end)

    addtrigger(id2,
    "^你略一凝神，精神看起来好多了。",
    function()
        if dushu then
        print(">>>>>>> dushu")
        dushu_worker()
    end
    end)
    
    addtrigger(id3,
    "^(你一觉醒来|你刚刚睡过一觉).*",--，精神抖擞地活动了几下手脚。",
    function()
        dushu=true
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        dushu_worker()
    end)
    
end)

add_alias("xx2", function(p)
    local id1="xx1"
    local id2="xx2"
    local id3="xx3"
    local id4="xx4"
    local id5="xx5"

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
   print(">>>>>>>>> time_lenth = "..tostring(time_lenth))
    
    local dushu=true
    local yungong=false
    local shuijiao=false
    local time_out=false

    local food=myvar["food"]
    local lian=myvar["lian"]
    local book=myvar["book"]
    local shifu=myvar["shifu"]
    -- local xuecmd=myvar["xuecmd"]

    food=food or "mantou"
    lian=lian or "dodge"
    book=book or "huntian-qigong"
    shifu=shifu or "shifu"

    function dushu_worker()
        if time_out then
            return
        end
        if dushu then
            dushu=false
            yungong=true
            shuijiao=false
            --------------
            watch_dog=false
            send("xue "..shifu.." for "..book.." 50")
        end
    end

    function shuijiao_worker()
        if time_out then
            return
        end
        dushu=false
        yungong=false
        shuijiao=false
        --------------
        watch_dog=false
        execs("drink;eat "..food..";lian "..lian.." 50;lian "..lian.." 50;sleep",1)
    end


    local watch_dog=true
    local watch_dog_cnt=0

    function watch_dog_reset()
        if time_out then
            return
        end
        watch_dog_cnt=watch_dog_cnt+1
        if watch_dog_cnt % 10 == 0 then
            send("save")
        end
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< watch_dog reset.")
        watch_dog=true
        add_timer(60,function()
            if watch_dog then
                dushu=true
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< watch_dog triggered")
                dushu_worker()
            end
            watch_dog_reset()
        end,"shediao_watchdog")
    end

    watch_dog_reset()
    dushu_worker()
    
    add_timer(time_lenth,function()
        time_out=true
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id2)
        deltrigger(id1)
        deltrigger(id3)
        if myvar["quit"]=="yes" then
            execs(";;;;;save;quit",10)
        else
            execs("jump;jump;jump;jump;jump;jump;save",10)
        end
    end,"shediao_timeout")
    
    addtrigger(id1,"^(你今天太累了|你已经很累了|你现在过于疲倦).*",--，无法专心下来研读新知。
    function()
        if time_out then
            return
        end
        if yungong then
            yungong=false
            dushu=true
            shuijiao=true
            print("<<<<<<<<<<<<<<<<<<  yungong.")
            add_timer(3, function()
                if shuijiao then
                    shuijiao_worker()
                end
            end,uuid())
            watch_dog=false
            execs("yun regenerate")
        end
    end)

    addtrigger(id2,
    "^你略一凝神，精神看起来好多了。",
    function()
        if dushu then
        print(">>>>>>> dushu")
        dushu_worker()
    end
    end)
    
    addtrigger(id3,
    "^(你一觉醒来|你刚刚睡过一觉).*",--，精神抖擞地活动了几下手脚。",
    function()
        dushu=true
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        dushu_worker()
    end)
    
end)

add_alias("tn", function(p)
    local id1="lg1"
    local id2="lg2"
    local id3="lg3"
    local id4="lg4"
    local id5="lg5"
    local cnt=0
    local shuijiao=false

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end
    
    print(">>>>>>> tuna 300")
    send("tuna 300")
    
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id1)
        deltrigger(id2)
        deltrigger(id3)
        deltrigger(id4)
        deltrigger(id5)
        execs("jump;jump;jump;jump",20)
    end,uuid())
    
    addtrigger(id1,
    "^你吐纳完毕，睁开双眼.*",
    function()
        print(">>>>>>> yun and tu ")
            add_timer(3, function()
                if shuijiao then
                    shuijiao=false
                    send("sleep")
                end
            end,uuid())
           shuijiao=true
           send("yun regenerate")
        -- execs("yun regenerate;tuna 200",2)
        -- send("da")
    end)
    
    -- addtrigger(id2,
    -- "你现在的气太少了，无法产生内息运行全身经脉。",
    -- function()
    --     print(">>>>>>> sleep")
    --     cnt=cnt+1
    --     if cnt%30==0 then
    --         send("save")
    --     end
    --     execs(";drink;eat mantou;sleep",1)
    --     -- send("sleep");
    -- end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< wake")
        print(">>>>>>> tu")
        send("tuna 300")

    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        execs("drink;eat mantou;tuna 20",5)
    end)
    
    local cnt=0

    addtrigger(id5,"^你略一凝神.*",function()
        shuijiao=false
        cnt=cnt+1
        if cnt%100==0 then
            execs("save;tuna 200",1)
        else
            if cnt%7==0 then
                execs("drink;eat mantou;tuna 200",2)
            else
                send("tuna 200")
            end
        end
        -- execs("yun regenerate;dazuo 20",1)
    end)
        
end)
