-- function mysplit (inputstr, sep)
--        if sep == nil then
--                  sep = "%s"
--                     end
--                        local t={}
--                           for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
--                                     table.insert(t, str)
--                                        end
--                                           return t
--                                       end
--
function string_codelist(inputstr)
    inputstr = inputstr or ""
    -- print(">>>>> integer "..inputstr)
    local len = #inputstr
    t={}
    for i=1,len do
        table.insert(t, string.byte(inputstr,i))
        -- print(">>>>> byte: "..tostring(t[i]))
    end
    return t,len
end

function find_substring(s1, s2)
    local t1,l1=string_codelist(s1)
    local t2,l2=string_codelist(s2)
   -- print(">>>>> len of two strings: "..tostring(l1).." "..tostring(l2))
   if l1<l2 then
       return false
   end
    for i=1,l1-l2+1 do
        local found = true
        for j=1,l2 do
            if t1[i+j-1] ~= t2[j] then
                found = false
                break
            end
        end
        if found then
            return true
        end
    end
    return false
end

-- add_trigger("room_name","^[> ]*(\\S.*\\S)\\s+-(\\s*\\[.*\\]\\s*|\\s*|\\s*0|\\s*★)$",function (p)
--
addtrigger("dingwei1","^(.*)◆(.*)$", function(p)
    print("<<<<<<<<<<<< triggered")
    close_trigger("dingwei1")
    -- local area =p[1]-- trim(p[2])
    var.area2=tostring(p[1])..tostring(p[2])
    for k,v in pairs(full_zonename) do
        if find_substring(var.area2,v) then
            var.area=v
        end
    end
end)

addtrigger("dingwei2", "你说道：「dingwei」", 
    function()
        close_trigger("dingwei2")
        print(">>>>> room name: "..var.roomname)
        print(">>>>> room description: "..var.roomdesc)
        print(">>>>> area :"..tostring(var.area))
        print(">>>>> area2: "..tostring(var.area2))

        local name=var.roomname
        local desc=var.roomdesc
        local res=0
        for k,v in pairs(rooms) do
            if rawequal(name,v.name) then
                -- if find_substring(v.area,var.area) or find_substring(var.area,v.area) then
                if rawequal(var.area,v.area) then
                    print("<<<<<<<<<<<< dingwei "..tostring(v.id))
                    exe("say roomat"..tostring(v.id))
                end
            end
        end
    end)

function dingwei()
    open_trigger("dingwei1")
    open_trigger("dingwei2")
    execs("look;lm;q;say dingwei",2)
end

add_alias("dingwei", function()
    -- local id=
    dingwei()
    -- print(">>>>>>>dingwei: "..tostring(id))

end)

close_trigger("dingwei1")
close_trigger("dingwei2")

