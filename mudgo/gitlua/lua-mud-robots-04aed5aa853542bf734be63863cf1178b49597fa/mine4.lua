
function keep_trying(cmds,end_trigger,t)
    t=t or 1
    local on=true

    local function trying()
        if on then
            print(">>>> run command "..cmds)
            execs(cmds,1)
            add_timer(t,function()
                print(">>>> time to run again")
                trying()
            end,uuid())
        end
    end

    addtrigger("trying",end_trigger,
    function()
        on=false
        deltrigger("trying")
        print(">>>> done trying "..cmds)
    end)

    trying()
end

function run_stages(stages)
    if max==0 then
        return
    end

    local function run_stage(i)
        
        if i>#stages then
            deltrigger("run_stage")
            return
        end

        addtrigger("run_stage",
            stages[i].end_trigger,
            function()
                print(">>>>>>> local stage "..tostring(i+1))
                run_stage(i+1)
            end)
        
        print(">>>> running stage "..tostring(i))
        stages[i].func()
    end
    
    run_stage(1)
end

-- add_alias("test_it",function()
--     print(">>>> start test ")
--            keep_trying("do 10 sw;do 10 se;do 10 su","山口两崖相对如门。",4)
--        end)

add_alias("yz_cd",function()
    stages={
       [1]={
       end_trigger="你顺利到达了终点。",
       func=function()
           execs("node walk yz_ca",0)
       end},
   [2]={
   end_trigger="你顺利到达了终点。",
   func=function()
       execs("node walk ca_cd",0)
   end},
   [3]={
   end_trigger="你从小船上跳了下来，到了汉水南渡。",
   func=function()
       execs("ride",0)
   end},
   [4]={
       end_trigger="这个方向没有出路。",
       func=function()
           execs("do 3 su")
       end},
    [5]={
    end_trigger="^剑门关 -",
       -- end_trigger="^山口两崖相对如门。",
       func=function()
           keep_trying("do 10 sw;do 10 se;do 10 su","^剑门关 -",4)--"^山口两崖相对如门。",4)
       end},
    [6]={
        end_trigger="^总督府门前.*",
        func=function()
           execs("sd;do 4 s",2)
       end}
   }
   run_stages(stages)
end)

add_alias("ga", function()
    execs("get all")
end)
add_alias("gac", function()
    execs("get all from corpse")
end)

add_alias("cd_yz",function()
    stages={
       [1]={
       end_trigger="^金牛道 -",
       func=function()
           execs("do 4 n;nu;nd",1)
       end},
   [2]={
       end_trigger="^汉水南渡 -.*",
       func=function()
           keep_trying("do 10 nw;do 10 ne;do 10 nd","^汉水南渡 -.*",4)
       end},
   [3]={
       end_trigger="你从小船上跳了下来，到了汉水北渡。",
       func=function()
           execs("ride",0)
   end},
   [4]={
       end_trigger="^朱雀大街 -.*",
       func=function()
           execs("do 10 n;nu;n;nu;do 4 ne;do 6 n")
       end},
    [5]={
       end_trigger="你顺利到达了终点。",
       func=function()
           execs("node walk ca_yz")
       end},
   }
   run_stages(stages)
end)

add_alias("zj_yz",function()
    stages={
       [1]={
       end_trigger="^西津渡口 -",
       func=function()
           execs("do 4 w;do 2 nw",1)
       end},
       [2]={
           end_trigger="^(一叶扁舟缓缓地驶了过来|岸边一只渡船上).*",
           -- end_trigger="^一叶扁舟缓缓地驶了过来，艄公将一块踏脚板搭上堤岸，以便乘客上下。",
           func=function()
               execs("yell boat;yell boat",2)
           end},
       [3]={
           end_trigger="^(艄公说|艄公要继续做生意).*",
           func=function()
               keep_trying("enter","^(艄公说|艄公要继续做生意).*",10)
       end},
       [4]={
           end_trigger="^中央广场 -.*",
           func=function()
               execs("out;nd;nw;nd;do 4 n")
           end},
   }
   run_stages(stages)
end)

add_alias("yz_zj",function()
    stages={
       [1]={
       end_trigger="^扬子津 -",
       func=function()
           execs("do 4 s;su;se;su",1)
       end},
   [2]={
       end_trigger="^(一叶扁舟缓缓地驶了过来|岸边一只渡船上).*",
       func=function()
           execs("yell boat;yell boat",2)
       end},
   [3]={
       end_trigger="^(艄公说|艄公要继续做生意).*",
       func=function()
           keep_trying("enter","^(艄公说|艄公要继续做生意).*",10)
   end},
    [4]={
       end_trigger="^广场 -.*",
       func=function()
           execs("out;do 2 se;do 4 e")
       end},
   }
   run_stages(stages)
end)
    -- 船老大 雷明(Lei ming)
function find_ship_and_pay(river_name)
    addtrigger("find_ship_boss",
    "^\ \ \ \ 船老大.*",
    function(p)
        deltrigger("find_ship_boss")
        -- name=string.sub(p[-1],string.find(name,"(")
        local v=p[-1]
        local fullname=string.sub(v,string.find(v,'%(')+1,string.find(v,'%)')-1)
        local name=string.sub(fullname,1,string.find(fullname,"\ ")-1):lower()
        print(">>>>>>>>>>>>>> boss name: "..name)
        execs("ask "..name.." about "..river_name..";yell boat;yell boat",2)
    end)
    send("look")
end

-- add_alias("testing",function()
--     find_ship_boss()
-- end)

-- 黄河渡口 -
add_alias("yz_bj",function()
    local stages={
       [1]={
       end_trigger="^黄河渡口 -",
       func=function()
           execs("node walk yz_qufudk",1)
       end},
   [2]={
       end_trigger="^(一叶扁舟缓缓地驶了过来|岸边一只渡船上).*",
       func=function()
           find_ship_and_pay("huanghe")
           -- execs("ask liang about huanghe;yell boat",2)
       end},
   [3]={
       end_trigger="^(艄公说|艄公要继续做生意).*",
       func=function()
           keep_trying("enter","^黄河渡船.*",10)
           -- keep_trying("enter","^(艄公说|艄公要继续做生意).*",10)
   end},
    [4]={
       end_trigger="^你顺利到达了终点。",
       func=function()
           keep_trying("node walk hhbkd3_bj","^你顺利到达了终点。",3)
           -- execs(";node walk hhbkd3_bj",3)
       end},
   }
   run_stages(stages)
end)

add_alias("bj_yz",function()
    local stages={
       [1]={
       end_trigger="^你顺利到达了终点。",
       -- end_trigger="^黄河渡口 -",
       func=function()
           execs("node walk bj_qf",1)
       end},
   [2]={
       end_trigger="^(一叶扁舟缓缓地驶了过来|岸边一只渡船上).*",
       func=function()
           find_ship_and_pay("huanghe")
           -- execs("ask liang about huanghe;yell boat",2)
       end},
   [3]={
       end_trigger="^(艄公说|艄公要继续做生意).*",
       func=function()
           -- execs("enter;enter;enter;enter",3)
           keep_trying("enter","^黄河渡船.*",10)
   end},
    [4]={
       end_trigger="^你顺利到达了终点。",
       func=function()
           -- execs(";node walk qufudk_yz",3)
           keep_trying("node walk qufudk_yz","^你顺利到达了终点。",3)
       end},
   }
   run_stages(stages)
end)

