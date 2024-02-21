
add_alias("dushu", function(p)
    local id1="lg1"
    local id2="lg2"
    local id3="lg3"
    local id4="lg4"
    
    local bookname="blade book"
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
       t=t or 0
       execs(";du "..bookname.." for 50",t)
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
    
    addtrigger(id1,
    -- "你运功完毕，深深吸了口气，站了起来。",
    ".*，似乎有点心得。$",
    function()
        worker()
    end)
    
    addtrigger(id2,
    -- "你现在的气太少了，无法产生内息运行全身经脉。",
    "你现在过于疲倦，无法专心下来研读新知。",
    function()
        print(">>>>>>> sleep")
        send("sleep");
    end)
    
    addtrigger(id3,
    "你一觉醒来，精神抖擞地活动了几下手脚。",
    function()
        worker()
    end)
    
    addtrigger(id4,
    "你刚刚睡过一觉, 多睡对身体有害无益!",
    function()
        worker(10);
    end)
    
    worker()

end)
