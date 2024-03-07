
add_alias("dushu_old", function(p)
    local id1="lg1"
    local id2="lg2"
    local id3="lg3"
    local id4="lg4"

    local bookname="sword book"
    -- local bookname="blade book"
    -- local bookname="shediao"
    local lian_what="dodge"
   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end 
    -- 你从身上拿出一本飞沙走石十三式准备好好研读。
    -- 你现在过于疲倦，无法专心下来研读新知。
    -- 你研读了九次有关基本刀法的技巧，似乎有点心得。
    -- >
    -- 本刀法的技巧，似乎有点心得。
   local function worker(t)
       t=t or 1
       execs("do 10 climb wall;du "..bookname.." for 50",t)
   end
    
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
   
    local ds1=false
    local ds2=true
    local ds3=false
    local ds4=false

    worker()

    addtrigger(id1,
    -- "你运功完毕，深深吸了口气，站了起来。",
    ".*，似乎有点心得。$",
    function()
        if ds1 then
            ds1=false
            ds2=true
            worker()
        end
    end)
    
    addtrigger(id2,
    -- "你现在的气太少了，无法产生内息运行全身经脉。",
    "你现在过于疲倦，无法专心下来研读新知。",
    function()
        if ds2 then
            ds2=false
            ds3=true
            ds4=true
            print(">>>>>>> sleep")
            execs("do 10 climb wall;sleep",1);
        end
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        if ds3 then
            ds3=false
            ds4=false
            ds2=true
            worker()
        end
    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        if ds4 then
            ds4=false
            ds3=false
            ds2=true
            execs("drink;eat mantou;hp;cha;do 10 climb wall;lian "..lian_what.." 50",1.5)
            worker(9);
        end
    end)
end)

function do_and_sleep(cmds,time_lenth)
    
    time_lenth=time_lenth or 0
    cmds=cmds or ""

    local id1=uuid()
    local id2=uuid()
    local id3=uuid()

    local busy=false
    local on=true

    local function worker(t)
       t=t or 1
       if busy then
           return
       end
       if on then
           busy=true
           execs(cmds..";say doagain",t)
       end
   end
    
----- TIME OUT Trigger
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        on=false
        deltrigger(id2)
        deltrigger(id1)
        deltrigger(id3)
        execs("jump;jump;jump;jump;jump;jump;jump",10)
    end,uuid())
   
    addtrigger(id3,
        "不一会儿，你就进入了梦乡。",
        function()
            busy=true
        end)

    addtrigger(id2,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        if on then
            busy=false
            worker()
        end
    end)

    addtrigger(id1,
    "你说道：「doagain」",
    function()
        if on then
            busy=false
            worker()
        end
    end)
    
    local function sleep_loop()
        if on then
            -- worker()
            add_timer(20,function()
                execs("drink;eat mantou;sleep",1)
                sleep_loop()
            end,uuid())
        end
    end

    sleep_loop()
    worker()
end

add_alias("paqiang", function(p)
    -- local bookname="sword book"
    -- local bookname="blade book"
    local bookname=myvar["book"]
    local lian_what=myvar["lian"]
    local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end 
    local cmds=""
    if bookname=="shediao" then
        cmds="read "..bookname.." 50;do 10 climb wall;lian "..lian_what.." 50"
    else
        cmds="du "..bookname.." for 50;do 10 climb wall;lian "..lian_what.." 50"
    end
    do_and_sleep(cmds,time_lenth)
end)

add_alias("pdiao", function(p)
    local id1="lg1"

   local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    end 
    
    add_timer(time_lenth,function()
        print(">>>>>>> deltrigger TIME UP.")
        deltrigger(id1)
        add_timer(30,function()
            send("jump")
        end,uuid())
    end,uuid())
   

    addtrigger(id1,
    -- "你运功完毕，深深吸了口气，站了起来。",
    "你凭吊完毕,站起身来",
    -- .*，似乎有点心得。$",
    function()
        execs(";pingdiao",1)
    end)
    send("pingdiao")

end)

