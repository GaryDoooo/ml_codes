function uuid()
    local random = math.random
    local template ='xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    return string.gsub(template, '[xy]', function (c)
        local v = (c == 'x') and random(0, 0xf) or random(8, 0xb)
        return string.format('%x', v)
    end)
end

GetUniqueNumber=uuid

function run2(clist,t,k,kmax)
    if k<=kmax then
        send(clist[k])
        addtimer(t,function()
            run2(clist,t,k+1,kmax)
        end,uuid())
    end
end

function execs(cmds,t,if_print)
    local if_print2 = if_print or 1
    local t2=t or 1
    local clist={}
    for match in string.gmatch(cmds..";","(.-);") do
        table.insert(clist,match)
    end
    local kmax=0
    for k,v in pairs(clist) do
        if if_print2==1 then
            print(">>>> "..v.." "..tostring(k))
        end
        kmax=k
    end
    run2(clist,t2,1,kmax)
end

addtrigger("continue_walk",
"你因为种种原因停了下来，可以用walk继续进行。",
function()
    execs(";walk",1)
    execs(";walk",6)
end)

add_alias("ls",function()
    send("yun recover")
end)

myvar={
    ["book"]="shediao",
    ["food"]="mantou",
    ["lian"]="dodge",
    ["quit"]="no",
    ["shifu"]="kuaihuo"
}

add_alias("setvar", function(p)
    local function trim(s)
          return s:match'^()%s*$' and '' or s:match'^%s*(.*%S)'
      end
    local parameters={}
    parameters[1],parameters[2]=p[-1]:match("(%w+)(.+)")

    print(">>>>>>> p1="..tostring(parameters[1]))
    print("<<<<<<<<<<<<<<<<<< p2="..tostring(parameters[2]))

    myvar[trim(parameters[1])]=trim(parameters[2])
end)

full_zonename = {
["扬州"] = "扬州",
["信阳"] = "信阳",
["杀手"] = "杀手帮",
["长江"] = "长江北岸",
["襄阳"] = "襄阳",
["武当"] = "武当山",
["小山"] = "小山村",
["华山"] = "华山",
["长安"] = "长安",
["洛阳"] = "洛阳",
["中原"] = "中原",
["少林"] = "少林寺",
["古墓"] = "古墓",
["全真"] = "全真",
["曲阜"] = "曲阜",
["泰山"] = "泰山",
["黄河"] = "黄河南岸",
["回疆"] = "回族小镇",
["回族"] = "回族小镇",
["回部"] = "回部",
["灵鹫"] = "灵鹫",
["灵州"] = "灵州",
["丐帮"] = "丐帮",
["麒麟"] = "麒麟村",
["大轮"] = "大轮寺",
["凌霄"] = "凌霄城",
["白驼"] = "白驼山",
["绝情"] = "绝情谷",
["黄河"] = "黄河北岸",
["丝绸"] = "丝绸之路",
["晋阳"] = "晋阳",
["北京"] = "北京",
["紫禁"] = "紫禁城",
["天坛"] = "天坛",
["康亲"] = "康亲王府",
["张家"] = "张家口",
["日月"] = "日月神教",
["明教"] = "明教",
["兰州"] = "兰州",
["湟中"] = "湟中",
["神龙"] = "神龙岛",
["长江"] = "长江",
["岳阳"] = "岳阳",
["桃源"] = "桃源",
["铁掌"] = "铁掌峰",
["南昌"] = "南昌",
["泉州"] = "泉州",
["福州"] = "福州",
["岳王"] = "岳王墓",
["临安"] = "临安府",
["西湖"] = "西湖",
["建康"] = "建康府南城",
["都统"] = "都统制府",
["建康"] = "建康府北城",
["江州"] = "江州",
["镇江"] = "镇江",
["苏州"] = "苏州",
["归云"] = "归云庄",
["姑苏"] = "姑苏慕容",
["嘉兴"] = "嘉兴",
["牙山"] = "牙山",
["桃花"] = "桃花岛",
["杭州"] = "杭州提督府",
["成都"] = "成都",
["峨嵋"] = "峨嵋",
["峨眉"] = "峨眉后山",
["天龙"] = "天龙寺",
["无量"] = "无量山",
["大理"] = "大理城中",
["昆明"] = "昆明",
["平西"] = "平西王府",
["荆州"] = "襄阳", -- 新增20180810
--
["北京"]="北京",
["凌霄城"]="凌霄城",
["襄阳"]="襄阳",
["湟中"]="湟中",
["桃花岛"]="桃花岛",
["古墓"]="古墓",
["回疆小镇"]="回族小镇",
["回族小镇"]="回族小镇",
["桃源"]="桃源",
["镇江"]="镇江",
["临安府"]="临安府",
["泰山"]="泰山",
["铁掌峰"]="铁掌峰",
["小山村"]="小山村",
["信阳"]="信阳",
["都统制府"]="都统制府",
["黄河北岸"]="黄河北岸",
["无量山"]="无量山",
["江州"]="江州",
["康亲王府"]="康亲王府",
["武当山"]="武当山",
["姑苏慕容"]="姑苏慕容",
["峨眉后山"]="峨眉后山",
["长江"]="长江",
["昆明"]="昆明",
["神龙岛"]="神龙岛",
["绝情谷"]="绝情谷",
["扬州"]="扬州",
["少林寺"]="少林寺",
["牙山"]="牙山",
["全真"]="全真",
["杀手帮"]="杀手帮",
["中原"]="中原",
["大轮寺"]="大轮寺",
["白驼山"]="白驼山",
["岳王墓"]="岳王墓",
["晋阳"]="晋阳",
["丝绸之路"]="丝绸之路",
["平西王府"]="平西王府",
["泉州"]="泉州",
["长安"]="长安",
["华山"]="华山",
["杭州提督府"]="杭州提督府",
["西湖"]="西湖",
["回部"]="回部",
["天龙寺"]="天龙寺",
["峨嵋"]="峨嵋",
["灵鹫"]="灵鹫",
["成都"]="成都",
["丐帮"]="丐帮",
["嘉兴"]="嘉兴",
["归云庄"]="归云庄",
["曲阜"]="曲阜",
["灵州"]="灵州",
["苏州"]="苏州",
["南昌"]="南昌",
["紫禁城"]="紫禁城",
["明教"]="明教",
["日月神教"]="日月神教",
["福州"]="福州",
["大理城中"]="大理城中",
["岳阳"]="岳阳",
["兰州"]="兰州",
["建康府北城"]="建康府北城",
["洛阳"]="洛阳",
["麒麟村"]="麒麟村",
["天坛"]="天坛",
["张家口"]="张家口",
}


