add_alias("prm",function()
    print(">>>>> room name: "..var.roomname)
    print(">>>>> room description: "..var.roomdesc)
    -- print(">>>>> room exists: "..var.roomexist)
end)

add_alias("huijia",function()
    execs("s;;;do 2 sd;;;do 2 wd;;;do 2 sd;;;e;;;do 3 sd;;;ed;;;do 2 e;;;su;;;enter dong;enter dong;enter dong;enter dong;do 3 ne;;;up",1)
end)

function my_find_path(start,target,max_step)
    max_step = max_step or 20
    local res=""
    if start<=0 or target<=0 then
        return res
    end
    local q={} -- room id 
    local fa={} -- idx of fa
    local move={} -- cmd from fa to room id
    local step={}
    table.insert(q,start)
    table.insert(fa,0)
    table.insert(move,"")
    table.insert(step,0)
    local in_q={}
    in_q[start]=1
    local idx=0
    while idx<#q do
        idx=idx+1
        local now=q[idx]
        if step[idx]<max_step then
            for k,nxt in pairs(rooms[now].exits) do
                if in_q[nxt]~=1 then
                    if nxt==target then
                        local steps={}
                        table.insert(steps,k)
                        while idx>0 do 
                            table.insert(steps,move[idx])
                            idx=fa[idx]
                        end
                        for i=#steps,1,-1 do
                            res=res..steps[i]..";"
                        end
                        return res
                    end
                    in_q[nxt]=1
                    table.insert(q,nxt)
                    table.insert(fa,idx)
                    table.insert(move,k)
                    table.insert(step,step[idx]+1)
                end
            end
        end
    end
end

function find_in_yz(target)
    for id,room in pairs(rooms) do
        if target==room.name and room.area=="扬州" then
            return id
        end
    end
    return 0
end

add_alias("zuojob",function(p)
    -- 左全对你说道：人人都知道我们丐帮消息天下最为灵通，打探消息就靠你们这些跑腿的了，你去北门打听(dating)些消息回来。
    -- execs(my_find_path(2016,40),2)
    local id1="zj1"
    local id2="zj2"
    local id3="zj3"
    local id4="zj4"
    
    local time_lenth=p[-1]
    if type(time_lenth)=="string" then
        time_lenth=tonumber(time_lenth)
    else
        time_lenth=300
    end

    -- local s="左全对你说道：人人都知道我们丐帮消息天下最为灵通，打探消息就靠你们这些跑腿的了，你去北门打听(dating)些消息回来。"
    -- print(string.find(s,"北门"))
    -- print(string.find(s,"打听"))
    -- print(string.sub(s,string.find(s,"你去")+6,string.find(s,"打听")-1))
    local target_id=0
    
    local zj1=true
    local zj2=false
    local zj3=false
    local zj4=false

    execs("ask zuo about job",3)

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

    addtrigger(id1,"^左全对你说道：人人都知道我们丐帮消息天下最为灵通.*",
        function(p)
            if zj1 then
                zj1=false
                zj2=true
                -- local s=tostring(p)
                for k,v in pairs(p) do
                    print(">>>>>>>> msg "..tostring(v))
                    local target=string.sub(v,string.find(v,"你去")+6,string.find(v,"打听")-1)
                    target_id=find_in_yz(target)
                    break
                end
                local path_go=my_find_path(2016,target_id)
                -- local path_bck=my_find_path(target_id,2016)
                path_go=path_go.."say wodaole"
                execs(path_go,3)
            end
        end)

    addtrigger(id2,"你说道：「wodaole」",
        function(p)
            if zj2 then
                zj3=true
                execs("dating;get all;say wodaole",3)
            end
        end)

    addtrigger(id3,    "你已经完成了打听消息的任务，可以回去复命了！",
        function(p)
            if zj3 then
                zj2=false
                zj4=true
                path_bck=my_find_path(target_id,2016)
                path_bck="l;l;l;"..path_bck.."say wohuilaile"
                execs(path_bck,3)
            end
        end)

    addtrigger(id4,"你说道：「wohuilaile」",
        function(p)
            if zj4 then
                zj4=false
                zj1=true
                execs("dazuo 20;dazuo 20;dazuo 20;dazuo 20;ask zuo about job",15)
            end
        end)

end)

