saynowtime = ""
import sys
import time as ti
import os
def hmprint(line,speed,flag=1):
    for i in range(len(line)):
        print("\r"+line[0:i+1],end="")
        ti.sleep(speed)
nowtime = ti.strftime('%H',ti.localtime())
nowtime = int(nowtime)
if nowtime > 0 and nowtime < 9:
    saynowtime = '早上好！'
elif nowtime > 9:
    if nowtime < 12:
        saynowtime = "上午好！"
    elif nowtime > 11:
        if nowtime < 18:
            saynowtime = "下午好！"
    elif nowtime > 18:
        if nowtime < 23:
            saynowtime = "晚上好！"
        else:
            saynowtime = "凌晨好！"
week = ti.strftime("%w",ti.localtime())
if week == '1':
    week = '一'
if week == '2':
    week = '二'
if week == '3':
    week = '三'
if week == '4':
    week = '四'
if week == '5':
    week = '五'
if week == '6':
    week = '六'
if week == '7':
    week = '日'
print("HugeMate 2.00.0 for Consumers, Build 47\n输入“help”或“帮助”查看帮助手册\nHugeMate智能机器人为您服务,",saynowtime,"\n今天是",ti.strftime("%Y",ti.localtime()),"年",ti.strftime("%m",ti.localtime()),"月",ti.strftime("%d",ti.localtime()),"日,","星期",week,ti.strftime(",""%H"":""%M",ti.localtime())," \n你好啊！")
wenti = ""
shifoujixu = "1"
while shifoujixu == "1":   
    wenti = input("[HM-2.00.0]请输入>>>")
    if wenti == "你好" or wenti == "Hello" or wenti == "Hello!" or wenti == "Hello！" or wenti == "你好!" or wenti == "您好" or wenti == "您好！":
        print("你好呀!")
        continue
        
    elif wenti == "帮助" or wenti == "help":
        print("\n\nHugeMate 2.00帮助手册\nHugeMate 是 HugeCode 项目的智能机器人。它可以陪你聊天，缓解你的疲劳。\n具体功能:\n1.计时器(输入计时器启用)\n2.计算器(输入计算器启用)\n3.记事本(输入记事本启用)\n4.笑话(输入让我心情好一点或笑话（此项在下一版本实现）启用)\n5.画兔子、图案等(输入画个图启用)\n6.有道翻译(输入翻译启用)\n7.pyHugeCode 交互界面(输入HCIS启用)\n8.超级多小游戏(输入游戏进入游戏大厅)\n\n操作:\nexit:退出程序\nbye:关闭程序（快速）\n如果出现Terminator正常，请重新运行！！！")
    
    elif wenti == "再见!" or wenti == "再见" or wenti == "bye" or wenti == "Bye" or wenti == "bye!" or wenti == "Bye!":
        print("再见!下次再找我吧！")
        print("感谢您使用HugeMate智能！再见！\n\n")
        ti.sleep(1)
        sys.exit()
    
    elif wenti == "额" or wenti == "e":
        print("额，有什么事让你不舒服？")
        
    elif "啊哈哈" in wenti:
        print("别傻笑啦")
    elif wenti == "E":
        print("别紧张，我一直在你旁边")
        
    elif "伤心"in wenti:
        print("唉，别伤心了，陪我说说话，你就会轻松些")
        
    elif "不公平"in wenti:
        print("没关系，我们一起继续走在人生的漫漫长路，有我陪伴，你不孤单！")
        
    elif "开心"in wenti and "我" in wenti:
        print("我也替你开心呢！")
        
    elif "读过"in wenti and "书" in wenti:
        print("我可是博览群书哦！")
    elif wenti == "计时器" or wenti == "计时":
        import winsound as ws
        shijian = input("计时多少秒?\n")
        shijianfu = int(shijian)
        shijianint = int(shijian)
        shijianzheng = 0
        for x in range(shijianint):
            ti.sleep(1)
            shijianzheng = shijianzheng + 1
            shijianfu = shijianfu - 1
            print("已计时：",shijianzheng//60,"分",shijianzheng%60,"秒","\n","剩余",shijianfu//60,"分",shijianfu%60,"秒\n")
        print("时间到啦！！！")
        print("时间到啦！！！")
        print("时间到啦！！！")
        ws.Beep(500,2000)
        shifoujixu = "1"
    elif wenti == "计算器" or wenti == "calculator" or wenti == "calc":
        sfjxjs = "1"
        if sfjxjs == "1":
            fst1 = input("请输入第一个数字：")
            fst = int(fst1)
            jjfh = input("请输入加减符号：")
            sec1 = input("请输入第二个数字：")
            sec = int(sec1)
            if jjfh == "+":
                print(fst,jjfh,sec,"=",fst+sec)
            if jjfh == "-":
                print(fst,jjfh,sec,"=",fst-sec)
            if jjfh == "*":
                print(fst,jjfh,sec,"=",fst*sec)
            if jjfh == "/":
                print(fst,"除以",sec,"=",fst/sec)
            if jjfh == "**":
                print(fst,"的",sec,"次方","=",fst**sec)
            if jjfh == "%":
                print(fst,"模",sec,"余",fst%sec)
            if jjfh == "//":
                print(fst,"除后取整",sec,"=",fst//sec)
            if jjfh == "\\":
                print(fst,"除",sec,"=",sec/fst)
        shifoujixu = "1"
        continue
    elif wenti == 'oh':
        print("怎么了？")
        shifoujixu = "1"
        continue
    elif wenti == '你' or wenti== "you":
        print("我？？")
        shifoujixu = "1"
        continue
    elif wenti == '0/0' or wenti == "0除0" or wenti == '0÷0'  or wenti =="0除以0":
        hmprint("假设你有0块饼干，分给0位朋友，请问每个朋友能分到几块饼干？瞧，这个问题没劲儿，既没有饼干，也没有朋友。\n",0.2)
        shifoujixu = "1"
        continue
    elif wenti == "记事本":
        from tkinter import *
        from tkinter.filedialog import *
        from tkinter.messagebox import *
        import os
        
        filename=""
        showinfo(title="作者",message="HugeCode")
        
        def power():
            showinfo(title="版权信息",message="2020,张呈宇©")
        
        def joinhc():
            showinfo(title = "欢迎加入HugeCode！",message = "具体请咨询,QQ:908137590")
        
        def mynew():
            global top,filename,textPad
            top.title("未命名文件")
            filename=None
            textPad.delete(1.0,END)
        
        def myopen():
            global filename
            filename=askopenfilename(defaultextension=".txt")
            if filename=="":
                filename=None
            else:
                top.title("记事本--"+os.path.basename(filename))
                textPad.delete(1.0,END)
                f=open(filename,'r')
                textPad.insert(1.0,f.read())
                f.close()
        
        def mysave():
            global filename
            try:
                f=open(filename,'w')
                msg=textPad.get(1.0,'end')
                f.write(msg)
                f.close()
            except:
                mysaveas()
        
        def mysaveas():
            global filename
            f=asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
            filename=f
            fh=open(f,'w')
            msg=textPad.get(1.0,END)
            fh.write(msg)
            fh.close()
            top.title("记事本--"+os.path.basename(f))
        
        def cut():
            global textPad
            textPad.event_generate("<<Cut>>")
        
        def copy():
            global textPad
            textPad.event_generate("<<Copy>>")
        
        def paste():
            global textPad
            textPad.event_generate("<<Paste>>")
        
        def undo():
            global textPad
            textPad.event_generate("<<Undo>>")
        
        def redo():
            global textPad
            textPad.event_generate("<<Redo>>")
        
        def select_all():
            global textPad
            # textPad.event_generate("<<Cut>>")
            textPad.tag_add("sel","1.0","end")
        
        def find():
            t=Toplevel(top)
            t.title("查找")
            t.geometry("260x60+200+250")
            t.transient(top)
            Label(t,text="查找：").grid(row=0,column=0,sticky="e")
            v=StringVar()
            e=Entry(t,width=20,textvariable=v)
            e.grid(row=0,column=1,padx=2,pady=2,sticky="we")
            e.focus_set()
            c=IntVar()
            Checkbutton(t,text="不区分大小写",variable=c).grid(row=1,column=1,sticky='e')
            Button(t,text="查找所有",command=lambda:search(v.get(),c.get(),textPad,t,e)).grid(row=0,column=2,sticky="e"+"w",padx=2,pady=2)
            def close_search():
                textPad.tag_remove("match","1.0",END)
                t.destroy()
            t.protocol("WM_DELETE_WINDOW",close_search)
        
        def mypopup(event):
            # global editmenu
            editmenu.tk_popup(event.x_root,event.y_root)
        
        def search(needle,cssnstv,textPad,t,e):
            textPad.tag_remove("match","1.0",END)
            count=0
            if needle:
                pos="1.0"
                while True:
                    pos=textPad.search(needle,pos,nocase=cssnstv,stopindex=END)
                    if not pos:break
                    lastpos=pos+str(len(needle))
                    textPad.tag_add("match",pos,lastpos)
                    count+=1
                    pos=lastpos
                textPad.tag_config('match',fg='yellow',bg="green")
                e.focus_set()
                t.title(str(count)+"个被匹配")
        
        top=Tk()
        top.title("记事本")
        top.geometry("1000x600+100+50")
        
        menubar=Menu(top)
        
        # 文件功能
        filemenu=Menu(top)
        filemenu.add_command(label="新建",accelerator="Ctrl+N",command=mynew)
        filemenu.add_command(label="打开",accelerator="Ctrl+O",command=myopen)
        filemenu.add_command(label="保存",accelerator="Ctrl+S",command=mysave)
        filemenu.add_command(label="另存为",accelerator="Ctrl+shift+s",command=mysaveas)
        menubar.add_cascade(label="文件",menu=filemenu)
        
        # 编辑功能
        editmenu=Menu(top)
        editmenu.add_command(label="撤销",accelerator="Ctrl+Z",command=undo)
        editmenu.add_command(label="重做",accelerator="Ctrl+Y",command=redo)
        editmenu.add_separator()
        editmenu.add_command(label="剪切",accelerator="Ctrl+X",command=cut)
        editmenu.add_command(label="复制",accelerator="Ctrl+C",command=copy)
        editmenu.add_command(label="粘贴",accelerator="Ctrl+V",command=paste)
        editmenu.add_separator()
        editmenu.add_command(label="查找",accelerator="Ctrl+F",command=find)
        editmenu.add_command(label="全选",accelerator="Ctrl+A",command=select_all)
        menubar.add_cascade(label="编辑",menu=editmenu)
        
        # 关于 功能
        aboutmenu=Menu(top)
        aboutmenu.add_command(label="作者",command=author)
        aboutmenu.add_command(label="版权",command=power)
        aboutmenu.add_command(label="加入 HugeCode",command=joinhc)
        menubar.add_cascade(label="关于",menu=aboutmenu)
        top['menu']=menubar
        
        shortcutbar=Frame(top,height=25,bg='light sea green')
        shortcutbar.pack(expand=NO,fill=X)
        Inlabe=Label(top,width=2,bg='antique white')
        Inlabe.pack(side=LEFT,anchor='nw',fill=Y)
        
        textPad=Text(top,undo=True)
        textPad.pack(expand=YES,fill=BOTH)
        scroll=Scrollbar(textPad)
        textPad.config(yscrollcommand=scroll.set)
        scroll.config(command=textPad.yview)
        scroll.pack(side=RIGHT,fill=Y)
        
        # 热键绑定
        textPad.bind("<Control-N>",mynew)
        textPad.bind("<Control-n>",mynew)
        textPad.bind("<Control-O>",myopen)
        textPad.bind("<Control-o>",myopen)
        textPad.bind("<Control-S>",mysave)
        textPad.bind("<Control-s>",mysave)
        textPad.bind("<Control-A>",select_all)
        textPad.bind("<Control-a>",select_all)
        textPad.bind("<Control-F>",find)
        textPad.bind("<Control-f>",find)
        
        textPad.bind("<Button-3>",mypopup)
        top.mainloop()
    elif wenti == "学生管理":
        import sys
        def meun():
            menu_info = '''＋－－－－－－－－－－－－－－－－－－－－－－＋
        ｜            HugeCode 学生管理模块          ｜
        ｜ 1.添加学生                                ｜
        ｜ 2.显示所有学生                            ｜
        ｜ 3.删除学生信息                             ｜
        ｜ 4.修改学生信息                             ｜
        ｜ 5.按学生成绩顺序显示学生信息              ｜
        ｜ 6.按学生成绩倒序显示学生信息             ｜
        ｜ 7.按学生年龄顺序显示学生信息             ｜
        ｜ 8.按学生年龄倒序显示学生信息             ｜
        ｜ 9.将学生信息保存到学生信息.txt           ｜
        ｜ 10.从学生信息.txt文件中读取数据          ｜
        ｜ 11.退出主程序                          ｜
        ＋－－－－－－－－－－－－－－－－－－－－－－＋
        '''
            print(menu_info)
        
        
        # 以下二个函数用于sorted排序，　key的表达式函数
        def get_age(*l):
            for x in l:
                return x.get("age")
        def get_score(*l):
            for x in l:
                return x.get("score")
                
        # １）添加学生信息
        def add_student_info():
            L = []
            while True:
                n = input("请输入名字：")
                if not n:  # 名字为空　跳出循环
                    break
                try:
                    a = int(input("请输入年龄："))
                    s = int(input("请输入成绩："))
                except:
                    print("输入无效，不是整形数值．．．．重新录入信息")
                    continue
                info = {"name":n,"age":a,"score":s}
                L.append(info)
            print("学生信息录入完毕！！！")
            return L
        
        # ２）显示所有学生的信息
        def show_student_info(student_info):
            if not student_info:
                print("无数据信息．．．．．")
                return
            print("名字".center(8),"年龄".center(4),"成绩".center(4))
            for info in student_info:
                print(info.get("name").center(10),str(info.get("age")).center(4),str(info.get("score")).center(4))
        
        # ３）删除学生信息
        def del_student_info(student_info,del_name = ''):
            if not del_name:
                del_name = input("请输入删除的学生姓名：")
            for info in student_info:
                if del_name == info.get("name"):
                    return info
            raise IndexError("学生信息不匹配,没有找到%s" %del_name)
        
        # ４）修改学生信息
        def mod_student_info(student_info):
            mod_name = input("请输入修改的学生姓名：")
            for info in student_info:
                if mod_name == info.get("name"):
                    a = int(input("请输入年龄："))
                    s = int(input("请输入成绩："))
                    info = {"name":mod_name,"age":a,"score":s}
                    return info
            raise IndexError("学生信息不匹配,没有找到%s" %mod_name)
        
        # ５）按学生成绩高－低显示学生信息
        def score_reduce(student_info):
            print("按学生成绩高－低显示")
            mit = sorted(student_info ,key = get_score,reverse = True)
            show_student_info(mit)
        
        # ６）按学生成绩低－高显示学生信息
        def score_rise(student_info):
            print("按学生成绩低－高显示")
            mit = sorted(student_info ,key = get_score)
            show_student_info(mit)
        
        # ７）按学生年龄高－低显示学生信息
        def age_reduce(student_info):   
            print("按学生年龄高－低显示：")
            mit = sorted(student_info ,key = get_age,reverse = True)
            show_student_info(mit)
        
        # ８）按学生年龄低－高显示学生信息
        def age_rise(student_info): 
            print("按学生年龄低－高显示：")
            mit = sorted(student_info ,key = get_age)
            show_student_info(mit)
        
        # ９）保存学生信息到文件（students.txt)
        def save_info(student_info):
            try:
                students_txt = open("学生信息.txt","w")     # 以写模式打开，并清空文件内容
            except Exception as e:
                students_txt = open("学生信息.txt", "x")    # 文件不存在，创建文件并打开
            for info in student_info:
                students_txt.write(str(info)+"\n")          # 按行存储，添加换行符
            students_txt.close()
        
        # １０）从文件中读取数据（students.txt) 
        def read_info():
            old_info = []
            try:
                students_txt = open("学生信息.txt")
            except:
                print("暂未保存数据信息!")                       # 打开失败，文件不存在说明没有数据保存
                return
            while True:
                info = students_txt.readline()
                if not info:
                    break
                # print(info)
                info = info.rstrip()    #　去掉换行符
                # print(info)
                info = info[1:-1]       # 去掉｛｝
                # print(info)
                student_dict = {}       # 单个学生字典信息
                for x in info.split(","):   # 以，为间隔拆分
                    # print(x)
                    key_value = []      # 开辟空间，key_value[0]存key,key_value[0]存value
                    for k in x.split(":"):  # 以：为间隔拆分
                        k = k.strip()       #　去掉首尾空字符
                        # print(k)
                        if k[0] == k[-1] and len(k) > 2:        # 判断是字符串还是整数
                            key_value.append(k[1:-1])           # 去掉　首尾的＇
                        else:
                            key_value.append(int(k))
                        # print(key_value)
                    student_dict[key_value[0]] = key_value[1]   # 学生信息添加
                # print(student_dict)
                old_info.append(student_dict)   # 所有学生信息汇总
            students_txt.close()  
            return old_info   
        
        def main():
            student_info = []
            while True:
                # print(student_info)
                meun()
                number = input("请输入选项：")
                if number == '1':
                    student_info = add_student_info()
                elif number == '2':
                    show_student_info(student_info)
                elif number == '3':
                    try:
                        student_info.remove(del_student_info(student_info))
                    except Exception as e:
                        # 学生姓名不匹配
                        print(e)            
                elif number == '4':
                    try:                
                        student = mod_student_info(student_info)
                    except Exception as e:
                        # 学生姓名不匹配
                        print(e)
                    else:
                        # 首先按照根据输入信息的名字，从列表中删除该生信息，然后重新添加该学生最新信息
                        student_info.remove(del_student_info(student_info,del_name = student.get("name")))  
                        student_info.append(student)
                elif number == '5':
                    score_reduce(student_info)
                elif number == '6':
                    score_rise(student_info)
                elif number == '7':
                    age_reduce(student_info)
                elif number == '8':
                    age_rise(student_info)
                elif number == '9':
                    save_info(student_info)
                elif number == '10':
                    student_info = read_info()
                elif number == '11':
                    sys.exit()
                else:
                    break
                input("回车显示菜单:")
        
        main()
    elif wenti == "让我心情好一点":
        hmprint("打架用砖乎，不宜乱乎，照脸乎，使劲乎，乎不着，再乎，右手乎完左手乎，板砖乎断用鞋乎，既然乎，岂可一人独乎，有朋一起乎，不亦乐乎，乎着，往死里乎，乎不死还乎，乎死者，英雄也。乎不死，拉倒也。你明乎，不明乎？明乎则以，不明乎拿砖照己脸乎，一呼则明！",0.2)
    elif wenti == "画个图" or wenti == "画个图我看看":
        import turtle as t
        import random as rd
        randomjieguo = rd.randint(1,9)
        if randomjieguo == 1:
            list1 = ["cyan","red","yellow","green","blue","purple","pink","brown","black"]
            for i in range(300):
                t.pencolor(rd.choice(list1))
                t.forward(i)
                t.left(85)
                t.speed(0)
        if randomjieguo == 2:
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            for i in range(300):
                t.pencolor(rd.choice(list2))
                t.forward(i)
                t.left(91)
                t.speed(0)
        if randomjieguo == 3:
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            for i in range(300):
                t.pencolor(rd.choice(list2))
                t.forward(i)
                t.left(120)
                t.speed(0)
        if randomjieguo == 4:
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            for i in range(300):
                t.pencolor(rd.choice(list2))
                t.forward(i)
                t.left(72)
                t.speed(0)
        if randomjieguo == 5:
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            for i in range(rd.randint(255,355)):
                t.pencolor(rd.choice(list2))
                t.forward(i)
                t.left(rd.randint(15,175))
                t.speed(0)
        if randomjieguo == 6:
            import turtle as t
            import random as rd
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            t.speed(0)
            for i in range(rd.randint(20,50)):
                for x in range(36):
                    t.pencolor(rd.choice(list2))
                    t.forward(10)
                    t.left(10)
                    t.speed(0)
                t.forward(10)
        if randomjieguo == 7:
            import turtle as t
            import random as rd
            list2 = ["cyan","red","yellow","green","blue","purple","pink","brown"]
            t.speed(0)
            for i in range(18):
                for x in range(36):
                    t.pencolor(rd.choice(list2))
                    t.forward(10)
                    t.left(10)
                    t.speed(0)
                t.forward(10)
                t.left(20)
        if randomjieguo == 8:
        
            from turtle import *
            pensize(5)
            speed(0)
            ##color('#F4A460')#橘黄
            ##color('#FFE4E1')#肉粉
             
            ##【背景圆】
            color('#B088FF')#浅紫
            pu()
            goto(0,-200)
            pd()
            begin_fill()
            circle(200)
            end_fill()
             
            ##定义画弧函数
            def Arc(initial_degree,range_num,step,rotate_degree):
                seth(initial_degree)
                for n in range(range_num):   
                    fd(step)
                    rt(rotate_degree)#   
             
            ##定义填充矩形函数
            def Rect(x,y,height,width):
                pu()
                goto(x,y)
                pd()
                begin_fill()
                goto(x+width,y)
                goto(x+width,y+height)
                goto(x,y+height)
                goto(x,y)
                end_fill()
             
            ##定义绘制填充等边三角形函数    
            def Triangle(x,y,side_length):#等边三角形底边左角
                pu()
                goto(x,y)
                pd()
                begin_fill()
                seth(0)
                fd(side_length)
                rt(120)#lt()是正立三角形
                fd(side_length)
                rt(120)#lt()是正立三角形
                fd(side_length)
                end_fill()
                
            #中轴线——辅助绘图线
            #color("green")
            #Rect(-200,0,1,400)#x轴
            #Rect(0,-200,400,1)#y轴
             
            ##【图层1——面部轮廓】
            color('#F4A460')#橘黄
            #左耳
            pu()
            goto(-83.13,-10.94)
            pd()
            begin_fill()
             
            Arc(120,145,1,1/4)
            goto(-30,50)
            end_fill()
             
            #右耳
            pu()
            goto(83.13,-10.94)#(88.13,10.94)
            pd()
            begin_fill()
            Arc(60,145,1,-1/4)
            goto(30,50)
            end_fill()
             
            #腮帮
            #右腮帮
            pu()
            goto(83.13,-10.94)#0
            pd()
            begin_fill()
            Arc(-35,135,1,9/11)#1
            #print(pos())
             
            #下巴
            #pencolor("yellow")
            Arc(-145,70,1,3/10)#右半下颌2
            #print(pos())
             
            #pencolor("red")
            Arc(-175,40,1,1/5)#下巴连接线3
            #print(pos())
             
            #pencolor("pink")
            Arc(168,70,1,3/10)#左半下颌4
            #print(pos())
             
            #左腮帮
            #pencolor("grey")
            Arc(146,135,1,9/11)#5
            #print(pos())
             
            #两耳连接
            pu()
            goto(-30,50)
            Arc(15,80,1,1/2)
             
            end_fill()
             
             
            ##【图层2——耳部轮廓】
            color('pink')#FFC0CB
            #左耳
            pu()
            goto(-42,50)
            pd()
            begin_fill()
            Arc(-164,55,1,-7/8)
            Arc(120,100,1,1/3)
            goto(-42,50)
            end_fill()
             
            #右耳
            pu()
            goto(42,50)
            pd()
            begin_fill()
            Arc(-16,55,1,7/8)#(81.13,15.94)
            #print(pos())
            Arc(60,100,1,-1/3)#(104.15,111.82)
            #print(pos())
            goto(42,50)
            end_fill()
             
               
            ##【图层3——眼部轮廓】
            #左黑眼豆豆
            pu()
            goto(-46,-8)
            pd()
            color("black")
            seth(180)
            len = 0.3
            begin_fill()
            for k in range(2):         # 双弧绘制椭圆   
                for j in range(60):
                    if j < 30:
                        len += 0.04
                    else:
                        len -= 0.04
             
                    fd(len)
                    lt(3)
            end_fill()
            #左眼白光
            color("white")
            Rect(-43,-38,6,2)
             
            #右黑眼豆豆
            pu()
            goto(46,-8)
            pd()
            color("black")
            seth(180)
            len = 0.3
            begin_fill()
            for k in range(2):         # 将相同的动作重复做一遍
                for j in range(60):
                    if j < 30:
                        len += 0.04
                    else:
                        len -= 0.04
             
                    fd(len)
                    lt(3)
            end_fill()
            #右眼白光
            color("white")
            Rect(40,-38,6,2)
             
            ##【图层4——白鼻子轮廓】
            pu()
            goto(10,50)
            pd()
            goto(-10,50)
            color("white")
            begin_fill()
            Arc(-82,140,1,1/7)#结束角度A=-82-140*1/7=-102
            Arc(-112,20,1.1,-1.2)#结束角度B=-112+20*1.2=-88
            #setx(-xcor())
            goto(-xcor(),ycor())
            seth
            Arc(88,20,1.1,-1.2)#求A的y轴对称角度
            Arc(102,140,1,1/7)#求8的y轴对称角度
            goto(10,50)
            end_fill()
            pd()
             
            #圆嘴
            pu()
            goto(0,-150)
            seth(0)
            pd()
            begin_fill()
            circle(35)
            end_fill()
             
            #黑鼻头
            color("black")
            Triangle(-10,-120,20)
             
            end_fill()
             
            hideturtle()
            done()
        if randomjieguo == 9:
            #绘制大耳朵兔
            from turtle import *
            speed(10)
             
            #小兔的面部
            color('pink')
            pensize(5)
            circle(radius=100)#脸
             
            #眼睛
            pencolor('black')
            #左眼
            pu()
            goto(-45,92)
            pd()
            begin_fill()
            color((0,0,0),(0,0,0.1))
            circle(radius=15)
            #右眼
            pu()
            goto(45,92)
            pd()
            circle(radius=15)
            end_fill()
             
            #鼻子
            pu()
            goto(20,60)
            color('pink')
            pd()
            begin_fill()
            goto(-20,60)
            goto(0,45)
            goto(20,60)
            end_fill()
             
            #嘴
            goto(0,45)
            goto(0,40)
            seth(-90)
            circle(10,120)
            pu()
            goto(0,40)
            seth(-90)
            pd()
            circle(-10,120)
             
             
            #小兔的耳朵
            #左耳
            pu()
            goto(-60,180)#
            seth(200)
            pd()
            circle(radius=350,extent=90)
            goto(-98,110)
            #右耳
            pu()
            goto(60,180)#
            seth(-20)
            pd()
            circle(radius=-350,extent=90)
            goto(98,110)
             
            #小兔的身体
            pu()
            goto(20,3)
            seth(-25)
            pd()
            circle(radius=-250,extent=25)
            circle(radius=-135,extent=260)
            seth(50)
            circle(radius=-250,extent=25)
             
            ##小兔的胳膊
            #左臂
            pu()
            seth(180)
            goto(-30,-3)
            pd()
            #小短胳膊
            ##circle(radius=270,extent=20)
            ##circle(radius=20,extent=190)
            circle(radius=248,extent=30)
            circle(radius=29,extent=185)
            #右臂
            pu()
            seth(0)
            goto(30,-3)
            pd()
            circle(radius=-248,extent=30)
            circle(radius=-27,extent=184)
             
            ##小兔的脚
            ##左脚
            pu()
            goto(-162,-260)#
            pd()
            seth(0)
            circle(radius=41)
            #右脚
            pu()
            goto(164,-260)
            pd()
            circle(radius=41)
             
            done()
    elif wenti == '1/0' or wenti == "1除0" or wenti == '1÷0'  or wenti =="1除以0":
        hmprint("假设你有1块饼干，要分给多达0位朋友，那么问题来了，每位朋友能分到几块饼干？————看到了吧，这个问题没有意义，小朋友。然后饼干怪兽就把饼干全吃光了。啊呜。\n",0.2)
        shifoujixu = "1"
        continue
    elif wenti == "翻译" or wenti == 'translate':
        import json
        import requests
        # 翻译函数，word 需要翻译的内容
        def translate(word):
            # 有道词典 api
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
            # 传输的参数，其中 i 为需要翻译的内容
            key = {
                'type': "AUTO",
                'i': word,
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "ue": "UTF-8",
                "action": "FY_BY_CLICKBUTTON",
                "typoResult": "true"
            }
            # key 这个字典为发送给有道词典服务器的内容
            response = requests.post(url, data=key)
            # 判断服务器是否相应成功
            if response.status_code == 200:
                # 响应结果
                return response.text
            else:
                print("有道词典调用失败")
                # 响应失败就返回空
                return None
        
        def get_reuslt(repsonse):
            # 通过 json.loads 把返回的结果加载成 json 格式
            result = json.loads(repsonse)
            print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
            print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
        
        def main():
            print("""---有道翻译Python版---
中文自动翻译成英文，其他语言自动翻译为中文
需要退出请随便输入一次即可返回HugeMate""")
            word = input('翻译内容...')
            word = word + " "
            list_trans = translate(word)
            get_reuslt(list_trans)
        
        if __name__ == '__main__':
            main()
    elif wenti =="exit" or wenti == "Exit"  or wenti == "EXIT":
        hmprint("保存中,请稍等...\n",0.05)
        hmprint("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n",0.05,)
        from tqdm import tqdm
        for i in tqdm(range(100)):
             ti.sleep(0.02)
        print("\n")
        print("感谢您使用HugeMate智能！再见！\n\n")
        ti.sleep(1)
        sys.exit()
    elif "数学" in wenti and "喜欢" in wenti:
        print("我会编程，很喜欢数学")
    
    elif wenti == "编程" or wenti == "HugeCode" or wenti == "HCIS":
        # -*- coding: utf-8 -*-
        import time as ti
        def hmprint(line,speed,flag=1):
            for i in range(len(line)):
                print("\r"+line[0:i+1],end="")
                ti.sleep(speed)
        hmprint("-----HugeCode Interactive Shell in Py(pyHugeCode) 1.0-----\n",0.1)
        continuehcis = 1
        def hcisexit():
            cuntinuehcis = 0
            print()
        def hprint(text):
            print(text)
        def calc(item):
            print(item)
        def run(filename):
            runfile(filename)
        def port(thing):
            if thing == "drawing":
                import turtle as drawing
                print("Drawing ported!")
            elif thing == "time":
                import time
                print("Time ported!")
            elif thing == "random":
                import random
                print("Random ported!")
        runcode = ""
        while continuehcis == 1 and runcode != "hcisexit()":
            runcode = input("[HCIS1.0]>>>")
            try:
                runwrite = open("tmp.py","w")
            except Exception as e:
                runwrite = open("tmp.py","x")
            runwrite.write('''def hcisexit():
    cuntinuehcis = 0
    print()
def hprint(text):
    print(text)
def calc(item):
    print(item)
def run(filename):
    runfile(filename)
def port(thing):
    if thing == "drawing":
        import turtle as drawing
        print("Drawing ported!")
    elif thing == "time":
        import time
        print("Time ported!")
    elif thing == "random":
        import random
        print("Random ported!")\n''')
            runwrite.write(runcode)
            runwrite.close()
            runfile("tmp.py")

    elif wenti == "游戏":
        print("""小游戏列表
1.俄罗斯方块
2.飞机大战
3.2048
4.打砖块
5.双人飞行棋
6.井字棋
7.扫雷
8.愤怒的小鸟
9.贪吃蛇
10.吃豆人
11.大炮
12.飞翔的小球（飞翔的小鸟改编）
13.乒乓球
输入相应序号进入
小提示：请单击游戏界面开始交互游戏哦！""")

        gamechoice = input("请输入>>>")
        gamechoice = int(gamechoice)
        if gamechoice == 1:
            """
            ZetCode PyQt5 tutorial 
            This is a Tetris game clone.
            
            Author: Jan Bodnar
            Website: zetcode.com 
            Last edited: August 2017
            """
            
            from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
            from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
            from PyQt5.QtGui import QPainter, QColor 
            import sys, random
            
            class Tetris(QMainWindow):
                
                def __init__(self):
                    super().__init__()
                    
                    self.initUI()
                    
                    
                def initUI(self):    
                    '''initiates application UI'''
            
                    self.tboard = Board(self)
                    self.setCentralWidget(self.tboard)
            
                    self.statusbar = self.statusBar()        
                    self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
                    
                    self.tboard.start()
                    
                    self.resize(180, 380)
                    self.center()
                    self.setWindowTitle('Tetris')        
                    self.show()
                    
            
                def center(self):
                    '''centers the window on the screen'''
                    
                    screen = QDesktopWidget().screenGeometry()
                    size = self.geometry()
                    self.move((screen.width()-size.width())/2, 
                        (screen.height()-size.height())/2)
                    
            
            class Board(QFrame):
                
                msg2Statusbar = pyqtSignal(str)
                
                BoardWidth = 10
                BoardHeight = 22
                Speed = 300
            
                def __init__(self, parent):
                    super().__init__(parent)
                    
                    self.initBoard()
                    
                    
                def initBoard(self):     
                    '''initiates board'''
            
                    self.timer = QBasicTimer()
                    self.isWaitingAfterLine = False
                    
                    self.curX = 0
                    self.curY = 0
                    self.numLinesRemoved = 0
                    self.board = []
            
                    self.setFocusPolicy(Qt.StrongFocus)
                    self.isStarted = False
                    self.isPaused = False
                    self.clearBoard()
                    
                    
                def shapeAt(self, x, y):
                    '''determines shape at the board position'''
                    
                    return self.board[(y * Board.BoardWidth) + x]
            
                    
                def setShapeAt(self, x, y, shape):
                    '''sets a shape at the board'''
                    
                    self.board[(y * Board.BoardWidth) + x] = shape
                    
            
                def squareWidth(self):
                    '''returns the width of one square'''
                    
                    return self.contentsRect().width() // Board.BoardWidth
                    
            
                def squareHeight(self):
                    '''returns the height of one square'''
                    
                    return self.contentsRect().height() // Board.BoardHeight
                    
            
                def start(self):
                    '''starts game'''
                    
                    if self.isPaused:
                        return
            
                    self.isStarted = True
                    self.isWaitingAfterLine = False
                    self.numLinesRemoved = 0
                    self.clearBoard()
            
                    self.msg2Statusbar.emit(str(self.numLinesRemoved))
            
                    self.newPiece()
                    self.timer.start(Board.Speed, self)
            
                    
                def pause(self):
                    '''pauses game'''
                    
                    if not self.isStarted:
                        return
            
                    self.isPaused = not self.isPaused
                    
                    if self.isPaused:
                        self.timer.stop()
                        self.msg2Statusbar.emit("paused")
                        
                    else:
                        self.timer.start(Board.Speed, self)
                        self.msg2Statusbar.emit(str(self.numLinesRemoved))
            
                    self.update()
            
                    
                def paintEvent(self, event):
                    '''paints all shapes of the game'''
                    
                    painter = QPainter(self)
                    rect = self.contentsRect()
            
                    boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
            
                    for i in range(Board.BoardHeight):
                        for j in range(Board.BoardWidth):
                            shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                            
                            if shape != Tetrominoe.NoShape:
                                self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)
            
                    if self.curPiece.shape() != Tetrominoe.NoShape:
                        
                        for i in range(4):
                            
                            x = self.curX + self.curPiece.x(i)
                            y = self.curY - self.curPiece.y(i)
                            self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())
            
                                
                def keyPressEvent(self, event):
                    '''processes key press events'''
                    
                    if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
                        super(Board, self).keyPressEvent(event)
                        return
            
                    key = event.key()
                    
                    if key == Qt.Key_P:
                        self.pause()
                        return
                        
                    if self.isPaused:
                        return
                            
                    elif key == Qt.Key_Left:
                        self.tryMove(self.curPiece, self.curX - 1, self.curY)
                        
                    elif key == Qt.Key_Right:
                        self.tryMove(self.curPiece, self.curX + 1, self.curY)
                        
                    elif key == Qt.Key_Down:
                        self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
                        
                    elif key == Qt.Key_Up:
                        self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
                        
                    elif key == Qt.Key_Space:
                        self.dropDown()
                        
                    elif key == Qt.Key_D:
                        self.oneLineDown()
                        
                    else:
                        super(Board, self).keyPressEvent(event)
                            
            
                def timerEvent(self, event):
                    '''handles timer event'''
                    
                    if event.timerId() == self.timer.timerId():
                        
                        if self.isWaitingAfterLine:
                            self.isWaitingAfterLine = False
                            self.newPiece()
                        else:
                            self.oneLineDown()
                            
                    else:
                        super(Board, self).timerEvent(event)
            
                        
                def clearBoard(self):
                    '''clears shapes from the board'''
                    
                    for i in range(Board.BoardHeight * Board.BoardWidth):
                        self.board.append(Tetrominoe.NoShape)
            
                    
                def dropDown(self):
                    '''drops down a shape'''
                    
                    newY = self.curY
                    
                    while newY > 0:
                        
                        if not self.tryMove(self.curPiece, self.curX, newY - 1):
                            break
                            
                        newY -= 1
            
                    self.pieceDropped()
                    
            
                def oneLineDown(self):
                    '''goes one line down with a shape'''
                    
                    if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
                        self.pieceDropped()
                        
            
                def pieceDropped(self):
                    '''after dropping shape, remove full lines and create new shape'''
                    
                    for i in range(4):
                        
                        x = self.curX + self.curPiece.x(i)
                        y = self.curY - self.curPiece.y(i)
                        self.setShapeAt(x, y, self.curPiece.shape())
            
                    self.removeFullLines()
            
                    if not self.isWaitingAfterLine:
                        self.newPiece()
                        
            
                def removeFullLines(self):
                    '''removes all full lines from the board'''
                    
                    numFullLines = 0
                    rowsToRemove = []
            
                    for i in range(Board.BoardHeight):
                        
                        n = 0
                        for j in range(Board.BoardWidth):
                            if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                                n = n + 1
            
                        if n == 10:
                            rowsToRemove.append(i)
            
                    rowsToRemove.reverse()
                    
            
                    for m in rowsToRemove:
                        
                        for k in range(m, Board.BoardHeight):
                            for l in range(Board.BoardWidth):
                                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))
            
                    numFullLines = numFullLines + len(rowsToRemove)
            
                    if numFullLines > 0:
                        
                        self.numLinesRemoved = self.numLinesRemoved + numFullLines
                        self.msg2Statusbar.emit(str(self.numLinesRemoved))
                            
                        self.isWaitingAfterLine = True
                        self.curPiece.setShape(Tetrominoe.NoShape)
                        self.update()
                        
            
                def newPiece(self):
                    '''creates a new shape'''
                    
                    self.curPiece = Shape()
                    self.curPiece.setRandomShape()
                    self.curX = Board.BoardWidth // 2 + 1
                    self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
                    
                    if not self.tryMove(self.curPiece, self.curX, self.curY):
                        
                        self.curPiece.setShape(Tetrominoe.NoShape)
                        self.timer.stop()
                        self.isStarted = False
                        self.msg2Statusbar.emit("Game over")
            
            
            
                def tryMove(self, newPiece, newX, newY):
                    '''tries to move a shape'''
                    
                    for i in range(4):
                        
                        x = newX + newPiece.x(i)
                        y = newY - newPiece.y(i)
                        
                        if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                            return False
                            
                        if self.shapeAt(x, y) != Tetrominoe.NoShape:
                            return False
            
                    self.curPiece = newPiece
                    self.curX = newX
                    self.curY = newY
                    self.update()
                    
                    return True
                    
            
                def drawSquare(self, painter, x, y, shape):
                    '''draws a square of a shape'''        
                    
                    colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                                  0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
            
                    color = QColor(colorTable[shape])
                    painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
                        self.squareHeight() - 2, color)
            
                    painter.setPen(color.lighter())
                    painter.drawLine(x, y + self.squareHeight() - 1, x, y)
                    painter.drawLine(x, y, x + self.squareWidth() - 1, y)
            
                    painter.setPen(color.darker())
                    painter.drawLine(x + 1, y + self.squareHeight() - 1,
                        x + self.squareWidth() - 1, y + self.squareHeight() - 1)
                    painter.drawLine(x + self.squareWidth() - 1, 
                        y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)
            
            
            class Tetrominoe(object):
                
                NoShape = 0
                ZShape = 1
                SShape = 2
                LineShape = 3
                TShape = 4
                SquareShape = 5
                LShape = 6
                MirroredLShape = 7
            
            
            class Shape(object):
                
                coordsTable = (
                    ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
                    ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
                    ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
                    ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
                    ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
                    ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
                    ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
                    ((1, -1),    (0, -1),    (0, 0),     (0, 1))
                )
            
                def __init__(self):
                    
                    self.coords = [[0,0] for i in range(4)]
                    self.pieceShape = Tetrominoe.NoShape
            
                    self.setShape(Tetrominoe.NoShape)
                    
            
                def shape(self):
                    '''returns shape'''
                    
                    return self.pieceShape
                    
            
                def setShape(self, shape):
                    '''sets a shape'''
                    
                    table = Shape.coordsTable[shape]
                    
                    for i in range(4):
                        for j in range(2):
                            self.coords[i][j] = table[i][j]
            
                    self.pieceShape = shape
                    
            
                def setRandomShape(self):
                    '''chooses a random shape'''
                    
                    self.setShape(random.randint(1, 7))
            
                    
                def x(self, index):
                    '''returns x coordinate'''
                    
                    return self.coords[index][0]
            
                    
                def y(self, index):
                    '''returns y coordinate'''
                    
                    return self.coords[index][1]
            
                    
                def setX(self, index, x):
                    '''sets x coordinate'''
                    
                    self.coords[index][0] = x
            
                    
                def setY(self, index, y):
                    '''sets y coordinate'''
                    
                    self.coords[index][1] = y
            
                    
                def minX(self):
                    '''returns min x value'''
                    
                    m = self.coords[0][0]
                    for i in range(4):
                        m = min(m, self.coords[i][0])
            
                    return m
            
                    
                def maxX(self):
                    '''returns max x value'''
                    
                    m = self.coords[0][0]
                    for i in range(4):
                        m = max(m, self.coords[i][0])
            
                    return m
            
                    
                def minY(self):
                    '''returns min y value'''
                    
                    m = self.coords[0][1]
                    for i in range(4):
                        m = min(m, self.coords[i][1])
            
                    return m
            
                    
                def maxY(self):
                    '''returns max y value'''
                    
                    m = self.coords[0][1]
                    for i in range(4):
                        m = max(m, self.coords[i][1])
            
                    return m
            
                    
                def rotateLeft(self):
                    '''rotates shape to the left'''
                    
                    if self.pieceShape == Tetrominoe.SquareShape:
                        return self
            
                    result = Shape()
                    result.pieceShape = self.pieceShape
                    
                    for i in range(4):
                        
                        result.setX(i, self.y(i))
                        result.setY(i, -self.x(i))
            
                    return result
            
                    
                def rotateRight(self):
                    '''rotates shape to the right'''
                    
                    if self.pieceShape == Tetrominoe.SquareShape:
                        return self
            
                    result = Shape()
                    result.pieceShape = self.pieceShape
                    
                    for i in range(4):
                        
                        result.setX(i, -self.y(i))
                        result.setY(i, self.x(i))
            
                    return result
            
            
            if __name__ == '__main__':
                
                app = QApplication([])
                tetris = Tetris()    
                sys.exit(app.exec_())
        elif gamechoice == 2:
            #-*- coding: utf-8 -*-
            import pygame
            from sys import exit
            from pygame.locals import *
            import random
            
            # 设置游戏屏幕大小
            SCREEN_WIDTH = 480
            SCREEN_HEIGHT = 800
            
            # 子弹类
            class Bullet(pygame.sprite.Sprite):
                def __init__(self, bullet_img, init_pos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = bullet_img
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = init_pos
                    self.speed = 10
            
                def move(self):
                    self.rect.top -= self.speed
            
            # 玩家飞机类
            class Player(pygame.sprite.Sprite):
                def __init__(self, plane_img, player_rect, init_pos):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = []                                 # 用来存储玩家飞机图片的列表
                    for i in range(len(player_rect)):
                        self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
                    self.rect = player_rect[0]                      # 初始化图片所在的矩形
                    self.rect.topleft = init_pos                    # 初始化矩形的左上角坐标
                    self.speed = 8                                  # 初始化玩家飞机速度，这里是一个确定的值
                    self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合
                    self.is_hit = False                             # 玩家是否被击中
            
                # 发射子弹
                def shoot(self, bullet_img):
                    bullet = Bullet(bullet_img, self.rect.midtop)
                    self.bullets.add(bullet)
            
                # 向上移动，需要判断边界
                def moveUp(self):
                    if self.rect.top <= 0:
                        self.rect.top = 0
                    else:
                        self.rect.top -= self.speed
            
                # 向下移动，需要判断边界
                def moveDown(self):
                    if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
                        self.rect.top = SCREEN_HEIGHT - self.rect.height
                    else:
                        self.rect.top += self.speed
            
                # 向左移动，需要判断边界
                def moveLeft(self):
                    if self.rect.left <= 0:
                        self.rect.left = 0
                    else:
                        self.rect.left -= self.speed
            
                # 向右移动，需要判断边界        
                def moveRight(self):
                    if self.rect.left >= SCREEN_WIDTH - self.rect.width:
                        self.rect.left = SCREEN_WIDTH - self.rect.width
                    else:
                        self.rect.left += self.speed
            
            # 敌机类
            class Enemy(pygame.sprite.Sprite):
                def __init__(self, enemy_img, enemy_down_imgs, init_pos):
                   pygame.sprite.Sprite.__init__(self)
                   self.image = enemy_img
                   self.rect = self.image.get_rect()
                   self.rect.topleft = init_pos
                   self.down_imgs = enemy_down_imgs
                   self.speed = 2
            
                # 敌机移动，边界判断及删除在游戏主循环里处理
                def move(self):
                    self.rect.top += self.speed
            
            # 初始化 pygame
            pygame.init()
            
            # 设置游戏界面大小、背景图片及标题
            # 游戏界面像素大小
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            
            # 游戏界面标题
            pygame.display.set_caption('Python打飞机大战')
            
            # 背景图
            background = pygame.image.load('resources/image/background.png').convert()
            
            # Game Over 的背景图
            game_over = pygame.image.load('resources/image/gameover.png')
            
            # 飞机及子弹图片集合
            plane_img = pygame.image.load('resources/image/shoot.png')
            
            # 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
            player_rect = []
            player_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家飞机图片
            player_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸图片
            
            player_pos = [200, 600]
            player = Player(plane_img, player_rect, player_pos)
            
            # 子弹图片
            bullet_rect = pygame.Rect(1004, 987, 9, 21)
            bullet_img = plane_img.subsurface(bullet_rect)
            
            # 敌机不同状态的图片列表，包括正常敌机，爆炸的敌机图片
            enemy1_rect = pygame.Rect(534, 612, 57, 43)
            enemy1_img = plane_img.subsurface(enemy1_rect)
            enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))
            
            
            #存储敌机，管理多个对象
            enemies1 = pygame.sprite.Group()
            
            # 存储被击毁的飞机
            enemies_down = pygame.sprite.Group()
            
            # 初始化射击及敌机移动频率
            shoot_frequency = 0
            enemy_frequency = 0
            
            # 初始化分数
            score = 0
            
            # 游戏循环帧率设置
            clock = pygame.time.Clock()
            
            # 判断游戏循环退出的参数
            running = True
            
            # 游戏主循环
            while running:
                # 控制游戏最大帧率为 60
                clock.tick(60)
            
                # 生成子弹，需要控制发射频率
                # 首先判断玩家飞机没有被击中
                # 循环15次发射一个子弹
                if not player.is_hit:
                    if shoot_frequency % 15 == 0:
                        player.shoot(bullet_img)
                    shoot_frequency += 1
                    if shoot_frequency >= 15:
                        shoot_frequency = 0
            
                # 生成敌机，需要控制生成频率
                # 循环50次生成一架敌机
                if enemy_frequency % 50 == 0:
                    enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
                    enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
                    enemies1.add(enemy1)
                enemy_frequency += 1
                if enemy_frequency >= 100:
                    enemy_frequency = 0
            
                for bullet in player.bullets:
                    # 以固定速度移动子弹
                    bullet.move()
                    # 移动出屏幕后删除子弹
                    if bullet.rect.bottom < 0:
                        player.bullets.remove(bullet)   
            
                for enemy in enemies1:
                    #2. 移动敌机
                    enemy.move()
                    #3. 敌机与玩家飞机碰撞效果处理
                    if pygame.sprite.collide_circle(enemy, player):
                        enemies_down.add(enemy)
                        enemies1.remove(enemy)
                        player.is_hit = True
                        break
                    #4. 移动出屏幕后删除敌人
                    if enemy.rect.top < 0:
                        enemies1.remove(enemy)
            
                #敌机被子弹击中效果处理
                #将被击中的敌机对象添加到击毁敌机 Group 中
                enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
                for enemy_down in enemies1_down:
                    enemies_down.add(enemy_down)
            
                # 绘制背景
                screen.fill(0)
                screen.blit(background, (0, 0))
            
                # 绘制玩家飞机
                if not player.is_hit:
                    screen.blit(player.image[0], player.rect) #将正常飞机画出来
                else:
                    # 玩家飞机被击中后的效果处理
                    screen.blit(player.image[1], player.rect) #将爆炸的飞机画出来
                    running = False
            
                # 敌机被子弹击中效果显示
                for enemy_down in enemies_down:
                    enemies_down.remove(enemy_down)
                    score += 1
                    screen.blit(enemy_down.down_imgs, enemy_down.rect) #将爆炸的敌机画出来
            
            
                # 显示子弹
                player.bullets.draw(screen)
                # 显示敌机
                enemies1.draw(screen)
            
                # 绘制得分
                score_font = pygame.font.Font(None, 36)
                score_text = score_font.render('score: '+str(score), True, (128, 128, 128))
                text_rect = score_text.get_rect()
                text_rect.topleft = [10, 10]
                screen.blit(score_text, text_rect)
            
                # 更新屏幕
                pygame.display.update()
            
                # 处理游戏退出
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            
                # 获取键盘事件（上下左右按键）
                key_pressed = pygame.key.get_pressed()
            
                # 处理键盘事件（移动飞机的位置）
                if key_pressed[K_w] or key_pressed[K_UP]:
                    player.moveUp()
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    player.moveDown()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    player.moveLeft()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    player.moveRight()
            
            # 游戏 Game Over 后显示最终得分
            font = pygame.font.Font(None, 64)
            text = font.render('Final Score: '+ str(score), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(game_over, (0, 0))
            screen.blit(text, text_rect)
            
            # 显示得分并处理游戏退出
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                pygame.display.update()
        elif gamechoice == 3:
            # _*_ coding:UTF-8 _*_
            import numpy,sys,random,pygame
            from pygame.locals import*
            
            Size = 4                                          #4*4行列
            Block_WH = 110                                    #每个块的长度宽度
            BLock_Space = 10                                  #两个块之间的间隙
            Block_Size = Block_WH*Size+(Size+1)*BLock_Space
            Matrix = numpy.zeros([Size,Size])                 #初始化矩阵4*4的0矩阵
            Screen_Size = (Block_Size,Block_Size+110)
            Title_Rect = pygame.Rect(0,0,Block_Size,110)      #设置标题矩形的大小
            Score = 0
            
            Block_Color = {
                    0:(150,150,150),
                    2:(255,255,255),
                    4:(255,255,128),
                    8:(255,255,0),
                    16:(255,220,128),
                    32:(255,220,0),
                    64:(255,190,0),
                    128:(255,160,0),
                    256:(255,130,0),
                    512:(255,100,0),
                    1024:(255,70,0),
                    2048:(255,40,0),
                    4096:(255,10,0),
            }                                                     #数块颜色
            
            #基础类
            class UpdateNew(object):
            	"""docstring for UpdateNew"""
            	def __init__(self,matrix):
            		super(UpdateNew, self).__init__()
            		self.matrix = matrix
            		self.score  = 0
            		self.zerolist = []
            
            	def combineList(self,rowlist):
            		start_num = 0
            		end_num = Size-rowlist.count(0)-1
            		while start_num < end_num:
            			if rowlist[start_num] == rowlist[start_num+1]:
            				rowlist[start_num] *= 2
            				self.score += int(rowlist[start_num])                      #每次返回累加的分数
            				rowlist[start_num+1:] = rowlist[start_num+2:]
            				rowlist.append(0)
            			start_num += 1
            		return rowlist
            
            	def removeZero(self,rowlist):
            		while True:
            			mid = rowlist[:]                      #拷贝一份list
            			try:
            				rowlist.remove(0)
            				rowlist.append(0)
            			except:
            				pass
            			if rowlist == mid:
            				break;
            		return self.combineList(rowlist)
            
            	def toSequence(self,matrix):
            		lastmatrix = matrix.copy()
            		m,n = matrix.shape                                         #获得矩阵的行，列
            		for i in range(m):
            			newList = self.removeZero(list(matrix[i]))
            			matrix[i] = newList
            			for k in range(Size-1,Size-newList.count(0)-1,-1):     #添加所有有0的行号列号
            				self.zerolist.append((i,k))
            		if matrix.min() == 0 and (matrix!=lastmatrix).any():       #矩阵中有最小值0且移动后的矩阵不同，才可以添加0位置处添加随机数
            			GameInit.initData(Size,matrix,self.zerolist)
            		return matrix
            	                      
            
            class LeftAction(UpdateNew):
            	"""docstring for LeftAction"""
            	def __init__(self,matrix):
            		super(LeftAction, self).__init__(matrix)
            
            	def handleData(self):
            		matrix = self.matrix.copy()                               #获得一份矩阵的复制
            		newmatrix = self.toSequence(matrix)
            		return newmatrix,self.score
            
            class RightAction(UpdateNew):
            	"""docstring for RightAction"""
            	def __init__(self,matrix):
            		super(RightAction, self).__init__(matrix)
            
            	def handleData(self):
            		matrix = self.matrix.copy()[:,::-1]
            		newmatrix = self.toSequence(matrix)
            		return newmatrix[:,::-1],self.score
            
            class UpAction(UpdateNew):
            	"""docstring for UpAction"""
            	def __init__(self,matrix):
            		super(UpAction, self).__init__(matrix)
            
            	def handleData(self):
            		matrix = self.matrix.copy().T
            		newmatrix = self.toSequence(matrix)
            		return newmatrix.T,self.score
            
            
            class DownAction(UpdateNew):
            	"""docstring for DownAction"""
            	def __init__(self,matrix):
            		super(DownAction, self).__init__(matrix)
            
            	def handleData(self):
            		matrix = self.matrix.copy()[::-1].T
            		newmatrix = self.toSequence(matrix)
            		return newmatrix.T[::-1],self.score
            
            
            class GameInit(object):
            	"""docstring for GameInit"""
            	def __init__(self):
            		super(GameInit, self).__init__()
            
            	@staticmethod
            	def getRandomLocal(zerolist = None):
            		if zerolist == None:
            			a = random.randint(0,Size-1)
            			b = random.randint(0,Size-1)
            		else:
            			a,b = random.sample(zerolist,1)[0]
            		return a,b
            
            	@staticmethod
            	def getNewNum():                             #随机返回2或者4
            		n = random.random()
            		if n > 0.8:
            			n = 4
            		else:
            			n = 2
            		return n
            
            
            	@classmethod
            	def initData(cls,Size,matrix = None,zerolist = None):
            		if matrix is None:
            			matrix = Matrix.copy()
            		a,b = cls.getRandomLocal(zerolist)       #zerolist空任意返回(x,y)位置，否则返回任意一个0元素位置
            		n = cls.getNewNum()
            		matrix[a][b] = n
            		return matrix                           #返回初始化任意位置为2或者4的矩阵
            
            	@classmethod
            	def drawSurface(cls,screen,matrix,score):
            		pygame.draw.rect(screen,(255,255,255),Title_Rect)              #第一个参数是屏幕，第二个参数颜色，第三个参数rect大小，第四个默认参数
            		font1 = pygame.font.SysFont('simsun',48)
            		font2 = pygame.font.SysFont(None,32)
            		screen.blit(font1.render('Score:',True,(255,127,0)),(20,25))     #font.render第一个参数是文本内容，第二个参数是否抗锯齿，第三个参数字体颜色
            		screen.blit(font1.render('%s' % score,True,(255,127,0)),(170,25))
            		screen.blit(font2.render('up',True,(255,127,0)),(360,20))
            		screen.blit(font2.render('left  down  right',True,(255,127,0)),(300,50))
            		a,b = matrix.shape
            		for i in range(a):
            			for j in range(b):
            				cls.drawBlock(screen,i,j,Block_Color[matrix[i][j]],matrix[i][j])
            
            
            	@staticmethod
            	def drawBlock(screen,row,column,color,blocknum):
            		font = pygame.font.SysFont('stxingkai',80)
            		w = column*Block_WH+(column+1)*BLock_Space
            		h = row*Block_WH+(row+1)*BLock_Space+110
            		pygame.draw.rect(screen,color,(w,h,110,110))
            		if blocknum != 0:
            			fw,fh = font.size(str(int(blocknum)))
            			screen.blit(font.render(str(int(blocknum)),True,(0,0,0)),(w+(110-fw)/2,h+(110-fh)/2))
            
            	@staticmethod
            	def keyDownPressed(keyvalue,matrix):
            		if keyvalue == K_LEFT:
            			return LeftAction(matrix)
            		elif keyvalue == K_RIGHT:
            			return RightAction(matrix)
            		elif keyvalue == K_UP:
            			return UpAction(matrix)
            		elif keyvalue == K_DOWN:
            			return DownAction(matrix)
            
            	@staticmethod
            	def gameOver(matrix):
            		testmatrix = matrix.copy()
            		a,b = testmatrix.shape
            		for i in range(a):
            			for j in range(b-1):
            				if testmatrix[i][j] == testmatrix[i][j+1]:                    #如果每行存在相邻两个数相同，则游戏没有结束
            					print('游戏没有结束')
            					return False
            		for i in range(b):
            			for j in range(a-1):
            				if testmatrix[j][i] == testmatrix[j+1][i]:
            					print('游戏没有结束')
            					return False
            		print('游戏结束')
            		return True
            
            def main():
            	pygame.init()
            	screen = pygame.display.set_mode(Screen_Size,0,32)      #屏幕设置
            	matrix = GameInit.initData(Size)
            	currentscore = 0
            	GameInit.drawSurface(screen,matrix,currentscore)
            	pygame.display.update()
            	while True:
            		for event in pygame.event.get():
            			if event.type == pygame.QUIT:
            				pygame.quit()
            				sys.exit(0)
            			elif event.type == pygame.KEYDOWN:
            				actionObject = GameInit.keyDownPressed(event.key,matrix)     #创建各种动作类的对象
            				matrix,score = actionObject.handleData()                     #处理数据
            				currentscore += score   
            				GameInit.drawSurface(screen,matrix,currentscore)
            				if matrix.min() != 0:
            					GameInit.gameOver(matrix)
            		pygame.display.update()
            
            
            if __name__ == '__main__':
            	main()
        elif gamechoice == 4:
            #导入模块
            import pygame
            from pygame.locals import *
            import sys,random,time,math
            
            class GameWindow(object):
            	'''创建游戏窗口类'''
            	def __init__(self,*args,**kw):		
            		self.window_length = 600
            		self.window_wide = 500
            		#绘制游戏窗口，设置窗口尺寸
            		self.game_window = pygame.display.set_mode((self.window_length,self.window_wide))
            		#设置游戏窗口标题
            		pygame.display.set_caption("CatchBallGame")
            		#定义游戏窗口背景颜色参数
            		self.window_color = (135,206,250)
            
            	def backgroud(self):
            		#绘制游戏窗口背景颜色
            		self.game_window.fill(self.window_color)
            
            class Ball(object):
            	'''创建球类'''
            	def __init__(self,*args,**kw):
            		#设置球的半径、颜色、移动速度参数
            		self.ball_color = (255,215,0)		
            		self.move_x = 1
            		self.move_y = 1
            		self.radius = 10
            
            	def ballready(self):
            		#设置球的初始位置、
            		self.ball_x = self.mouse_x
            		self.ball_y = self.window_wide-self.rect_wide-self.radius
            		#绘制球，设置反弹触发条件			
            		pygame.draw.circle(self.game_window,self.ball_color,(self.ball_x,self.ball_y),self.radius)
            
            	def ballmove(self):
            		#绘制球，设置反弹触发条件			
            		pygame.draw.circle(self.game_window,self.ball_color,(self.ball_x,self.ball_y),self.radius)		
            		self.ball_x += self.move_x
            		self.ball_y -= self.move_y
            		#调用碰撞检测函数
            		self.ball_window()
            		self.ball_rect()
            		#每接5次球球速增加一倍
            		if self.distance < self.radius:
            			self.frequency += 1
            			if self.frequency == 5:
            				self.frequency = 0
            				self.move_x += self.move_x
            				self.move_y += self.move_y
            				self.point += self.point
            		#设置游戏失败条件
            		if self.ball_y > 520:
            			self.gameover = self.over_font.render("Game Over",False,(0,0,0))
            			self.game_window.blit(self.gameover,(100,130))
            			self.over_sign = 1
            
            class Rect(object):
            	'''创建球拍类'''
            	def __init__(self,*args,**kw):
            		#设置球拍颜色参数
            		self.rect_color = (255,0,0)
            		self.rect_length = 100
            		self.rect_wide = 10
            
            	def rectmove(self):
            		#获取鼠标位置参数
            		self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
            		#绘制球拍，限定横向边界					
            		if self.mouse_x >= self.window_length-self.rect_length//2:
            			self.mouse_x = self.window_length-self.rect_length//2
            		if self.mouse_x <= self.rect_length//2:
            			self.mouse_x = self.rect_length//2
            		pygame.draw.rect(self.game_window,self.rect_color,((self.mouse_x-self.rect_length//2),(self.window_wide-self.rect_wide),self.rect_length,self.rect_wide))
            
            class Brick(object):
            	def __init__(self,*args,**kw):
            		#设置砖块颜色参数
            		self.brick_color = (139,126,102)
            		self.brick_list = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
            		self.brick_length = 80
            		self.brick_wide = 20
            
            	def brickarrange(self):		
            		for i in range(5):
            			for j in range(6):
            				self.brick_x = j*(self.brick_length+24)
            				self.brick_y = i*(self.brick_wide+20)+40
            				if self.brick_list[i][j] == 1:
            					#绘制砖块
            					pygame.draw.rect(self.game_window,self.brick_color,(self.brick_x,self.brick_y,self.brick_length,self.brick_wide))					
            					#调用碰撞检测函数
            					self.ball_brick()										
            					if self.distanceb < self.radius:
            						self.brick_list[i][j] = 0
            						self.score += self.point
            		#设置游戏胜利条件
            		if self.brick_list == [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]:
            			self.win = self.win_font.render("You Win",False,(0,0,0))
            			self.game_window.blit(self.win,(100,130))
            			self.win_sign = 1
            
            class Score(object):
            	'''创建分数类'''
            	def __init__(self,*args,**kw):		
            		#设置初始分数
            		self.score = 0
            		#设置分数字体
            		self.score_font = pygame.font.SysFont('arial',20)
            		#设置初始加分点数
            		self.point = 1
            		#设置初始接球次数
            		self.frequency = 0
            
            	def countscore(self):
            		#绘制玩家分数			
            		my_score = self.score_font.render(str(self.score),False,(255,255,255))
            		self.game_window.blit(my_score,(555,15))
            
            class GameOver(object):
            	'''创建游戏结束类'''
            	def __init__(self,*args,**kw):
            		#设置Game Over字体
            		self.over_font = pygame.font.SysFont('arial',80)
            		#定义GameOver标识
            		self.over_sign = 0
            
            class Win(object):
            	'''创建游戏胜利类'''
            	def __init__(self,*args,**kw):
            		#设置You Win字体
            		self.win_font = pygame.font.SysFont('arial',80)
            		#定义Win标识
            		self.win_sign = 0
            
            class Collision(object):
            	'''碰撞检测类'''
            	#球与窗口边框的碰撞检测
            	def ball_window(self):
            		if self.ball_x <= self.radius or self.ball_x >= (self.window_length-self.radius):
            			self.move_x = -self.move_x
            		if self.ball_y <= self.radius:
            			self.move_y = -self.move_y
            
            	#球与球拍的碰撞检测
            	def ball_rect(self):
            		#定义碰撞标识
            		self.collision_sign_x = 0
            		self.collision_sign_y = 0
            
            		if self.ball_x < (self.mouse_x-self.rect_length//2):
            			self.closestpoint_x = self.mouse_x-self.rect_length//2
            			self.collision_sign_x = 1
            		elif self.ball_x > (self.mouse_x+self.rect_length//2):
            			self.closestpoint_x = self.mouse_x+self.rect_length//2
            			self.collision_sign_x = 2
            		else:
            			self.closestpoint_x = self.ball_x
            			self.collision_sign_x = 3
            
            		if self.ball_y < (self.window_wide-self.rect_wide):
            			self.closestpoint_y = (self.window_wide-self.rect_wide)
            			self.collision_sign_y = 1
            		elif self.ball_y > self.window_wide:
            			self.closestpoint_y = self.window_wide
            			self.collision_sign_y = 2
            		else:
            			self.closestpoint_y = self.ball_y
            			self.collision_sign_y = 3
            		#定义球拍到圆心最近点与圆心的距离
            		self.distance = math.sqrt(math.pow(self.closestpoint_x-self.ball_x,2)+math.pow(self.closestpoint_y-self.ball_y,2))
            		#球在球拍上左、上中、上右3种情况的碰撞检测
            		if self.distance < self.radius and self.collision_sign_y == 1 and (self.collision_sign_x == 1 or self.collision_sign_x == 2):
            			if self.collision_sign_x == 1 and self.move_x > 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_x == 1 and self.move_x < 0:
            				self.move_y = - self.move_y
            			if self.collision_sign_x == 2 and self.move_x < 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_x == 2 and self.move_x > 0:
            				self.move_y = - self.move_y
            		if self.distance < self.radius and self.collision_sign_y == 1 and self.collision_sign_x == 3:
            			self.move_y = - self.move_y
            		#球在球拍左、右两侧中间的碰撞检测
            		if self.distance < self.radius and self.collision_sign_y == 3:
            			self.move_x = - self.move_x
            
            	#球与砖块的碰撞检测
            	def ball_brick(self):
            		#定义碰撞标识
            		self.collision_sign_bx = 0
            		self.collision_sign_by = 0
            
            		if self.ball_x < self.brick_x:
            			self.closestpoint_bx = self.brick_x
            			self.collision_sign_bx = 1
            		elif self.ball_x > self.brick_x+self.brick_length:
            			self.closestpoint_bx = self.brick_x+self.brick_length
            			self.collision_sign_bx = 2
            		else:
            			self.closestpoint_bx = self.ball_x
            			self.collision_sign_bx = 3
            
            		if self.ball_y < self.brick_y:
            			self.closestpoint_by = self.brick_y
            			self.collision_sign_by = 1
            		elif self.ball_y > self.brick_y+self.brick_wide:
            			self.closestpoint_by = self.brick_y+self.brick_wide
            			self.collision_sign_by = 2
            		else:
            			self.closestpoint_by = self.ball_y
            			self.collision_sign_by = 3
            		#定义砖块到圆心最近点与圆心的距离
            		self.distanceb = math.sqrt(math.pow(self.closestpoint_bx-self.ball_x,2)+math.pow(self.closestpoint_by-self.ball_y,2))
            		#球在砖块上左、上中、上右3种情况的碰撞检测
            		if self.distanceb < self.radius and self.collision_sign_by == 1 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            			if self.collision_sign_bx == 1 and self.move_x > 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 1 and self.move_x < 0:
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 2 and self.move_x < 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 2 and self.move_x > 0:
            				self.move_y = - self.move_y
            		if self.distanceb < self.radius and self.collision_sign_by == 1 and self.collision_sign_bx == 3:
            			self.move_y = - self.move_y
            		#球在砖块下左、下中、下右3种情况的碰撞检测
            		if self.distanceb < self.radius and self.collision_sign_by == 2 and (self.collision_sign_bx == 1 or self.collision_sign_bx == 2):
            			if self.collision_sign_bx == 1 and self.move_x > 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 1 and self.move_x < 0:
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 2 and self.move_x < 0:
            				self.move_x = - self.move_x
            				self.move_y = - self.move_y
            			if self.collision_sign_bx == 2 and self.move_x > 0:
            				self.move_y = - self.move_y
            		if self.distanceb < self.radius and self.collision_sign_by == 2 and self.collision_sign_bx == 3:
            			self.move_y = - self.move_y
            		#球在砖块左、右两侧中间的碰撞检测
            		if self.distanceb < self.radius and self.collision_sign_by == 3:
            			self.move_x = - self.move_x
            
            class Main(GameWindow,Rect,Ball,Brick,Collision,Score,Win,GameOver):
            	'''创建主程序类'''
            	def __init__(self,*args,**kw):		
            		super(Main,self).__init__(*args,**kw)
            		super(GameWindow,self).__init__(*args,**kw)
            		super(Rect,self).__init__(*args,**kw)
            		super(Ball,self).__init__(*args,**kw)
            		super(Brick,self).__init__(*args,**kw)
            		super(Collision,self).__init__(*args,**kw)		
            		super(Score,self).__init__(*args,**kw)
            		super(Win,self).__init__(*args,**kw)
            		#定义游戏开始标识
            		start_sign = 0
            
            		while True:			
            			self.backgroud()
            			self.rectmove()
            			self.countscore()			
            			
            			if self.over_sign == 1 or self.win_sign == 1:
            				break
            			#获取游戏窗口状态
            			for event in pygame.event.get():
            				if event.type == pygame.QUIT:
            					sys.exit()
            				if event.type == MOUSEBUTTONDOWN:
            					pressed_array = pygame.mouse.get_pressed()
            					if pressed_array[0]:
            						start_sign = 1
            			if start_sign == 0:
            				self.ballready()
            			else:
            				self.ballmove()
            
            			self.brickarrange()
            
            			#更新游戏窗口
            			pygame.display.update()
            			#控制游戏窗口刷新频率
            			time.sleep(0.010)
            
            if __name__ == '__main__':
            	pygame.init()
            	pygame.font.init()
            	catchball = Main()
        elif gamechoice == 5:
            import random
            # 地图初始坐标
            Maps = [0] *100    
             
            # 玩家A和玩家B的初始坐标
            PlayerPos = [0]*2
            # 存储玩家姓名
            playerNames = [""] *2
             
            # 俩个玩家行动的标记
            Flags = [True]*2
             
            # 封装一个不换行的print
            def print_end(num):
                print(num,end="")
             
             
            def gameshow():
                """
                飞行棋游戏头
                """
                print('\033[1;31;m')
                print("*"*50)
                print('\033[1;32;m')
                print("*" * 50)
                print('\033[5;33;m')
                print("*" * 15 + "飞行棋爵士版 v1.0" + "*"*20)
                print('\033[1;34;m')
                print("*" * 50)
                print('\033[1;35;m')
                print("*" * 50)
            def chushihuamap():
                luckyturn_list = [3,15,33,36,45,71,89,95] # 幸运轮盘 ◎
                for number1 in luckyturn_list:
                    Maps[number1] = 1
             
                landmine_list = [7,19,39,67,77,97] # 地雷 ●
                for number2 in landmine_list:
                    Maps[number2] = 2
             
                pause_list = [2,5,9,31,37,56,87]  # 暂停 ▲
                for number3 in pause_list:
                    Maps[number3] = 3
             
                timeTunnel_list = [1,10,28,60,88,] # 时空隧道 卐
                for number4 in timeTunnel_list:
                    Maps[number4] = 4
            def drawstringmap(a):
                """
                 构造地图
                :param a: 0~99 的地图坐标
                :return: 返回地图坐标所在的 图
                """
                # 玩家A和玩家B在同一坐标用<>表示
                str = ""
                if PlayerPos[0] == PlayerPos[1] and PlayerPos[0] == a:
                    str = "<>"
                elif PlayerPos[0] == a:
                    str = "Ａ"
                elif PlayerPos[1] == a:
                    str = "Ｂ"
                else:
                    if Maps[a] == 0:
                        print_end('\033[1;32;m')
                        str = " □"
             
                    elif Maps[a] == 1:
                        print_end('\033[1;34;m')
                        str = " ◎"
             
                    elif Maps[a] == 2:
                        print_end('\033[1;31;m')
                        str = " ●"
             
                    elif Maps[a] == 3:
                        print_end('\033[1;35;m')
                        str = " ▲"
             
                    else:
                        print_end('\033[1;33;m')
                        str = "卐"
                return str
            def drawmap():
                print("玩家A和玩家B在同一位置时用<>表示")
                print("图例：幸运轮盘:◎  地雷:●  暂停:▲  时空隧道:卐")
                # 第一横行
                for a in range(0,30):
                    print_end(drawstringmap(a))
                print() # 第一横行结束后应该换行
                # 第一竖行
                for a in range(30,35):
                    for b in range(0,29):
                        print_end("  ")
                    print_end(drawstringmap(a))
                    print()
                # 第二横行
                a = 64
                while a >=35:
                    print_end(drawstringmap(a))
                    a -= 1
                print() # 换行
                # 第二竖行
                for a in range(65,70):
                    print(drawstringmap(a))
                # 第三竖行
                for a in range(70,100):
                    print_end(drawstringmap(a))
                # 画完最后一行应换行
                print()
            def playGame(playnumber):
                """
                 玩游戏
                :param playnumber: 玩家坐标
                """
                rNumber = random.randint(1,6)
                input()
                print("玩家{0}按下任意键开始掷骰子".format(playerNames[playnumber]))
                input()
                print("玩家{0}掷出了{1}".format(playerNames[playnumber],rNumber))
                PlayerPos[playnumber] += rNumber
                changePos()
                input()
                print("玩家{0}按任意键开始行动".format(playerNames[playnumber]))
                input()
                print("玩家{0}行动完了".format(playerNames[playnumber]))
                input()
                if Maps[PlayerPos[playnumber]] == 0:
                    print("玩家{0}踩到了方块，什么也没发生\n\n".format(playerNames[playnumber]))
                elif Maps[PlayerPos[playnumber]] == 1:
                    input_num = input("玩家{0}踩到了幸运轮盘，请选择  1.轰炸对方（后退6格） 2.交换位置".format(playerNames[playnumber]))
             
                    while True:
                        if input_num == "1":
                            print("玩家{0}被轰炸，后退6格\n".format(playerNames[1 - playnumber]))
                            PlayerPos[1 - playnumber] -= 6
                            changePos()
                            input()
                            break
                        elif input_num == "2":
                            print("玩家{0}选择交换位置\n".format(playerNames[playnumber]))
                            PlayerPos[playnumber],PlayerPos[1 - playnumber] = PlayerPos[1 - playnumber],PlayerPos[playnumber]
                            input("交换完成，按任意键继续游戏\n")
                            break
                        else:
                            input_num = input("只能输入 1.轰炸对方（后退6格） 2.交换位置 请重新输入\n")
             
                elif Maps[PlayerPos[playnumber]] == 2:
                    print("玩家{0}踩中了地雷，后退6格\n".format(playerNames[playnumber]))
                    PlayerPos[playnumber] -= 6
                    changePos()
                    input()
                elif Maps[PlayerPos[playnumber]] == 3:
                    print("玩家{0}暂停一回合\n".format(playerNames[playnumber]))
             
                    Flags[playnumber] = False
                    input()
                elif Maps[PlayerPos[playnumber]] == 4:
                    print("恭喜玩家{0}进入时空隧道，前进10步\n".format(playerNames[playnumber]))
                    PlayerPos[playnumber] += 10
                    changePos()
                    input()
                changePos()
                # TODO 清屏 。。。。。
                drawmap()
            def changePos():
                if PlayerPos[0] < 0:
                    PlayerPos[0] = 0
                if PlayerPos[0] >99:
                    PlayerPos[0] = 99
                if PlayerPos[1] < 0:
                    PlayerPos[1] = 0
                if PlayerPos[1] > 99:
                    PlayerPos[1] = 99
            def win():
                print('\033[5;33;m')
                print("*" * 80)
                print("                          ■                        ■               ■          ")
                print("        ■■■■■■■■     ■    ■                       ■                 ■         ")
                print("        ■      ■     ■    ■                     ■ ■         ■       ■         ")
                print("        ■      ■     ■■■■■■■■■■               ■   ■         ■       ■         ")
                print("        ■■■■■■■■    ■     ■                    ■■■■■■■■     ■       ■         ")
                print("        ■      ■   ■      ■                      ●■ ●       ■       ■         ")
                print("        ■      ■          ■                     ● ■  ●      ■       ■         ")
                print("        ■      ■     ■■■■■■■■■■■               ●  ■    ●    ■       ■         ")
                print("        ■■■■■■■■          ■                 ●     ■     ●   ■       ■         ")
                print("       ■       ■          ■                       ■         ■       ■         ")
                print("      ■        ■          ■                       ■         ■       ■         ")
                print("     ■         ■          ■                       ■         ■     ■ ■         ")
                print("    ■          ■    ■■■■■■■■■■■■■■                ■                 ■         ")
                print("*" * 80)
            def input_names():
                print('\033[1;34;m')
                playerNames[0] = input("请输入玩家A的姓名")
                while playerNames[0] == "":
                    playerNames[0] = input("玩家A的名字不能为空，请重新输入")
                playerNames[1] = input("请输入玩家B的姓名")
                while playerNames[1] =="" or playerNames[0] == playerNames[1]:
                    if playerNames[1] == "":
                        playerNames[1] = input("玩家B的名字不能为空，请重新输入")
                    else:
                        playerNames[1] = input("玩家A的名字不能和玩家B的名字一样，请重新输入")
            def a_and_b_plaing():
                while PlayerPos[0] < 99 and PlayerPos[1] < 99:
                    if Flags[0] == True:
                        playGame(0)
                    else:
                        Flags[0] = True
             
                    if PlayerPos[0] >= 99:
                        print("玩家{0}漂亮的赢了玩家{1}".format(playerNames[0], playerNames[1]))
                        break
             
                    if Flags[1] == True:
                        playGame(1)
                    else:
                        Flags[1] = True
             
                    if PlayerPos[1] >= 99:
                        print("玩家{0}无耻的赢了玩家{1}".format(playerNames[1], playerNames[0]))
                        break
             
            # TODO 怎么清空控制台
             
            # 开始游戏
            gameshow()
            input_names()
            print("玩家{0}的姓名用A表示".format(playerNames[0]))
            print("玩家{0}的姓名用B表示".format(playerNames[1]))
            chushihuamap()
            drawmap()
            # 玩家A和玩家B 都没有到达终点
            a_and_b_plaing()
            drawmap()
            win()
        elif gamechoice == 6:
            # 棋盘
            class Board(object):
                def __init__(self):
                    #self._board = '-'*9 # 坑！！
                    self._board = ['-' for _ in range(9)]
                    self._history = [] # 棋谱
                    
                # 按指定动作，放入棋子
                def _move(self, action, take):
                    if self._board[action] == '-':
                        self._board[action] = take
                        
                        self._history.append((action, take)) # 加入棋谱
                        
                # 撤销动作，拿走棋子
                def _unmove(self, action):
                    self._board[action] = '-'
                    
                    self._history.pop()
                        
                # 棋盘快照
                def get_board_snapshot(self):
                    return self._board[:]
                    
                # 取棋盘上的合法走法
                def get_legal_actions(self):
                    actions = []
                    for i in range(9):
                        if self._board[i] == '-':
                            actions.append(i)
                    return actions
                    
                # 判断走法是否合法
                def is_legal_action(self, action):
                    return self._board[action] == '-'
                    
                # 终止检测
                def teminate(self):
                    board = self._board
                    lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
                    
                    if ['X']*3 in lines or ['O']*3 in lines or '-' not in board:
                        return True 
                    else:
                        return False
                        
                # 胜负检查
                def get_winner(self):
                    board = self._board
                    lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
                    
                    if ['X']*3 in lines:
                        return 0 
                    elif ['O']*3 in lines:
                        return 1 
                    else:
                        return 2
                        
                # 打印棋盘
                def print_b(self):
                    board = self._board
                    for i in range(len(board)):
                        print(board[i], end='')
                        if (i+1)%3 == 0:
                            print()
                
                # 打印棋谱
                def print_history(self):
                    print(self._history)
             
             
            # 玩家
            class Player(object):
                '''
                玩家只做两件事：思考、落子
                    1. 思考 --> 得到走法
                    2. 落子 --> 执行走法，改变棋盘
                '''
                def __init__(self, take='X'): # 默认执的棋子为 take = 'X'
                    self.take=take
                
                def think(self, board):
                    pass
                    
                def move(self, board, action):
                    board._move(action, self.take)
             
             
            # 人类玩家
            class HumanPlayer(Player):
                def __init__(self, take):
                    super().__init__(take)
                
                def think(self, board):
                    while True:
                        action = input('Please input a num in 0-8:')
                        if len(action)==1 and action in '012345678' and board.is_legal_action(int(action)):
                            return int(action)
             
             
            # 电脑玩家
            class AIPlayer(Player):
                def __init__(self, take):
                    super().__init__(take)
                
                def think(self, board):
                    print('AI is thinking ...')
                    take = ['X','O'][self.take=='X']
                    player = AIPlayer(take)     # 假想敌！！！
                    _, action = self.minimax(board, player)
                    #print('OK')
                    return action
                    
                # 极大极小法搜索，α-β剪枝
                def minimax(self, board, player, depth=0) :
                    '''参考：https://stackoverflow.com/questions/44089757/minimax-algorithm-for-tic-tac-toe-python'''
                    if self.take == "O": 
                        bestVal = -10
                    else:
                        bestVal = 10
                        
                    if board.teminate() :
                        if board.get_winner() == 0 :
                            return -10 + depth, None
                        elif board.get_winner() == 1 :
                            return 10 - depth, None
                        elif board.get_winner() == 2 :
                            return 0, None
             
                    for action in board.get_legal_actions() : # 遍历合法走法
                        board._move(action, self.take)
                        val, _ = player.minimax(board, self, depth+1) # 切换到 假想敌！！！
                        board._unmove(action) # 撤销走法，回溯
                        
                        if self.take == "O" :
                            if val > bestVal:
                                bestVal, bestAction = val, action
                        else :
                            if val < bestVal:
                                bestVal, bestAction = val, action
                    
                    return bestVal, bestAction
             
             
             
            # 游戏
            class Game(object):
                def __init__(self):
                    self.board = Board()
                    self.current_player = None
                    
                # 生成玩家
                def mk_player(self, p, take='X'): # p in [0,1]
                    if p==0:
                        return HumanPlayer(take)
                    else:
                        return AIPlayer(take)
                        
                # 切换玩家
                def switch_player(self, player1, player2):
                    if self.current_player is None:
                        return player1
                    else:
                        return [player1, player2][self.current_player == player1]
                        
                # 打印赢家
                def print_winner(self, winner): # winner in [0,1,2]
                    print(['Winner is player1','Winner is player2','Draw'][winner])
             
                # 运行游戏
                def run(self):
                    ps = input("Please select two player's type:\n\t0.Human\n\t1.AI\nSuch as:0 0\n")
                    p1, p2 = [int(p) for p in ps.split(' ')]
                    player1, player2 = self.mk_player(p1, 'X'), self.mk_player(p2, 'O') # 先手执X，后手执O
                    
                    print('\nGame start!\n')
                    self.board.print_b() # 显示棋盘
                    while True:
                        self.current_player = self.switch_player(player1, player2) # 切换当前玩家
                        
                        action = self.current_player.think(self.board) # 当前玩家对棋盘进行思考后，得到招法
                        
                        self.current_player.move(self.board, action)   # 当前玩家执行招法，改变棋盘
                        
                        self.board.print_b() # 显示当前棋盘
                        
                        if self.board.teminate(): # 根据当前棋盘，判断棋局是否终止
                            winner = self.board.get_winner() # 得到赢家 0,1,2
                            break
                    
                    self.print_winner(winner)
                    print('Game over!')
                    
                    self.board.print_history()
                
                
            if __name__ == '__main__':
                Game().run()
        elif gamechoice == 7:
            import sys
            import time
            from enum import Enum
            import pygame
            from pygame.locals import *
            from mineblock import *
            
            
            # 游戏屏幕的宽
            SCREEN_WIDTH = BLOCK_WIDTH * SIZE
            # 游戏屏幕的高
            SCREEN_HEIGHT = (BLOCK_HEIGHT + 2) * SIZE
            
            
            class GameStatus(Enum):
                readied = 1,
                started = 2,
                over = 3,
                win = 4
            
            
            def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
                imgText = font.render(text, True, fcolor)
                screen.blit(imgText, (x, y))
            
            
            def main():
                pygame.init()
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.display.set_caption('扫雷')
            
                font1 = pygame.font.Font('resources/a.TTF', SIZE * 2)  # 得分的字体
                fwidth, fheight = font1.size('999')
                red = (200, 40, 40)
            
                # 加载资源图片，因为资源文件大小不一，所以做了统一的缩放处理
                img0 = pygame.image.load('resources/0.bmp').convert()
                img0 = pygame.transform.smoothscale(img0, (SIZE, SIZE))
                img1 = pygame.image.load('resources/1.bmp').convert()
                img1 = pygame.transform.smoothscale(img1, (SIZE, SIZE))
                img2 = pygame.image.load('resources/2.bmp').convert()
                img2 = pygame.transform.smoothscale(img2, (SIZE, SIZE))
                img3 = pygame.image.load('resources/3.bmp').convert()
                img3 = pygame.transform.smoothscale(img3, (SIZE, SIZE))
                img4 = pygame.image.load('resources/4.bmp').convert()
                img4 = pygame.transform.smoothscale(img4, (SIZE, SIZE))
                img5 = pygame.image.load('resources/5.bmp').convert()
                img5 = pygame.transform.smoothscale(img5, (SIZE, SIZE))
                img6 = pygame.image.load('resources/6.bmp').convert()
                img6 = pygame.transform.smoothscale(img6, (SIZE, SIZE))
                img7 = pygame.image.load('resources/7.bmp').convert()
                img7 = pygame.transform.smoothscale(img7, (SIZE, SIZE))
                img8 = pygame.image.load('resources/8.bmp').convert()
                img8 = pygame.transform.smoothscale(img8, (SIZE, SIZE))
                img_blank = pygame.image.load('resources/blank.bmp').convert()
                img_blank = pygame.transform.smoothscale(img_blank, (SIZE, SIZE))
                img_flag = pygame.image.load('resources/flag.bmp').convert()
                img_flag = pygame.transform.smoothscale(img_flag, (SIZE, SIZE))
                img_ask = pygame.image.load('resources/ask.bmp').convert()
                img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))
                img_mine = pygame.image.load('resources/mine.bmp').convert()
                img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))
                img_blood = pygame.image.load('resources/blood.bmp').convert()
                img_blood = pygame.transform.smoothscale(img_blood, (SIZE, SIZE))
                img_error = pygame.image.load('resources/error.bmp').convert()
                img_error = pygame.transform.smoothscale(img_error, (SIZE, SIZE))
                face_size = int(SIZE * 1.25)
                img_face_fail = pygame.image.load('resources/face_fail.bmp').convert()
                img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
                img_face_normal = pygame.image.load('resources/face_normal.bmp').convert()
                img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
                img_face_success = pygame.image.load('resources/face_success.bmp').convert()
                img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
                face_pos_x = (SCREEN_WIDTH - face_size) // 2
                face_pos_y = (SIZE * 2 - face_size) // 2
            
                img_dict = {
                    0: img0,
                    1: img1,
                    2: img2,
                    3: img3,
                    4: img4,
                    5: img5,
                    6: img6,
                    7: img7,
                    8: img8
                }
            
                bgcolor = (225, 225, 225)   # 背景色
            
                block = MineBlock()
                game_status = GameStatus.readied
                start_time = None   # 开始时间
                elapsed_time = 0    # 耗时
            
                while True:
                    # 填充背景色
                    screen.fill(bgcolor)
            
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = event.pos
                            x = mouse_x // SIZE
                            y = mouse_y // SIZE - 2
                            b1, b2, b3 = pygame.mouse.get_pressed()
                            if game_status == GameStatus.started:
                                # 鼠标左右键同时按下，如果已经标记了所有雷，则打开周围一圈
                                # 如果还未标记完所有雷，则有一个周围一圈被同时按下的效果
                                if b1 and b3:
                                    mine = block.getmine(x, y)
                                    if mine.status == BlockStatus.opened:
                                        if not block.double_mouse_button_down(x, y):
                                            game_status = GameStatus.over
                        elif event.type == MOUSEBUTTONUP:
                            if y < 0:
                                if face_pos_x <= mouse_x <= face_pos_x + face_size \
                                        and face_pos_y <= mouse_y <= face_pos_y + face_size:
                                    game_status = GameStatus.readied
                                    block = MineBlock()
                                    start_time = time.time()
                                    elapsed_time = 0
                                    continue
            
                            if game_status == GameStatus.readied:
                                game_status = GameStatus.started
                                start_time = time.time()
                                elapsed_time = 0
            
                            if game_status == GameStatus.started:
                                mine = block.getmine(x, y)
                                if b1 and not b3:       # 按鼠标左键
                                    if mine.status == BlockStatus.normal:
                                        if not block.open_mine(x, y):
                                            game_status = GameStatus.over
                                elif not b1 and b3:     # 按鼠标右键
                                    if mine.status == BlockStatus.normal:
                                        mine.status = BlockStatus.flag
                                    elif mine.status == BlockStatus.flag:
                                        mine.status = BlockStatus.ask
                                    elif mine.status == BlockStatus.ask:
                                        mine.status = BlockStatus.normal
                                elif b1 and b3:
                                    if mine.status == BlockStatus.double:
                                        block.double_mouse_button_up(x, y)
            
                    flag_count = 0
                    opened_count = 0
            
                    for row in block.block:
                        for mine in row:
                            pos = (mine.x * SIZE, (mine.y + 2) * SIZE)
                            if mine.status == BlockStatus.opened:
                                screen.blit(img_dict[mine.around_mine_count], pos)
                                opened_count += 1
                            elif mine.status == BlockStatus.double:
                                screen.blit(img_dict[mine.around_mine_count], pos)
                            elif mine.status == BlockStatus.bomb:
                                screen.blit(img_blood, pos)
                            elif mine.status == BlockStatus.flag:
                                screen.blit(img_flag, pos)
                                flag_count += 1
                            elif mine.status == BlockStatus.ask:
                                screen.blit(img_ask, pos)
                            elif mine.status == BlockStatus.hint:
                                screen.blit(img0, pos)
                            elif game_status == GameStatus.over and mine.value:
                                screen.blit(img_mine, pos)
                            elif mine.value == 0 and mine.status == BlockStatus.flag:
                                screen.blit(img_error, pos)
                            elif mine.status == BlockStatus.normal:
                                screen.blit(img_blank, pos)
            
                    print_text(screen, font1, 30, (SIZE * 2 - fheight) // 2 - 2, '%02d' % (MINE_COUNT - flag_count), red)
                    if game_status == GameStatus.started:
                        elapsed_time = int(time.time() - start_time)
                    print_text(screen, font1, SCREEN_WIDTH - fwidth - 30, (SIZE * 2 - fheight) // 2 - 2, '%03d' % elapsed_time, red)
            
                    if flag_count + opened_count == BLOCK_WIDTH * BLOCK_HEIGHT:
                        game_status = GameStatus.win
            
                    if game_status == GameStatus.over:
                        screen.blit(img_face_fail, (face_pos_x, face_pos_y))
                    elif game_status == GameStatus.win:
                        screen.blit(img_face_success, (face_pos_x, face_pos_y))
                    else:
                        screen.blit(img_face_normal, (face_pos_x, face_pos_y))
            
                    pygame.display.update()
            
            
            if __name__ == '__main__':
                main()
        elif gamechoice == 8:
            import pygame as pg
            from source.main import main
            
            if __name__=='__main__':
                main()
                pg.quit()
        elif gamechoice == 9:
            """Snake, classic arcade game.
            
            Exercises
            
            1. How do you make the snake faster or slower?
            2. How can you make the snake go around the edges?
            3. How would you move the food?
            4. Change the snake to respond to arrow keys.
            
            """
            
            from turtle import *
            from random import randrange
            from freegames import square, vector
            
            food = vector(0, 0)
            snake = [vector(10, 0)]
            aim = vector(0, -10)
            
            def change(x, y):
                "Change snake direction."
                aim.x = x
                aim.y = y
            
            def inside(head):
                "Return True if head inside boundaries."
                return -200 < head.x < 190 and -200 < head.y < 190
            
            def move():
                "Move snake forward one segment."
                head = snake[-1].copy()
                head.move(aim)
            
                if not inside(head) or head in snake:
                    square(head.x, head.y, 9, 'red')
                    update()
                    return
            
                snake.append(head)
            
                if head == food:
                    print('Snake:', len(snake))
                    food.x = randrange(-15, 15) * 10
                    food.y = randrange(-15, 15) * 10
                else:
                    snake.pop(0)
            
                clear()
            
                for body in snake:
                    square(body.x, body.y, 9, 'black')
            
                square(food.x, food.y, 9, 'green')
                update()
                ontimer(move, 100)
            
            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            listen()
            onkey(lambda: change(10, 0), 'Right')
            onkey(lambda: change(-10, 0), 'Left')
            onkey(lambda: change(0, 10), 'Up')
            onkey(lambda: change(0, -10), 'Down')
            move()
            done()
        elif gamechoice == 10:
            """Pacman, classic arcade game.
            
            Exercises
            
            1. Change the board.
            2. Change the number of ghosts.
            3. Change where pacman starts.
            4. Make the ghosts faster/slower.
            5. Make the ghosts smarter.
            
            """
            
            from random import choice
            from turtle import *
            from freegames import floor, vector
            
            state = {'score': 0}
            path = Turtle(visible=False)
            writer = Turtle(visible=False)
            aim = vector(5, 0)
            pacman = vector(-40, -80)
            ghosts = [
                [vector(-180, 160), vector(5, 0)],
                [vector(-180, -160), vector(0, 5)],
                [vector(100, 160), vector(0, -5)],
                [vector(100, -160), vector(-5, 0)],
            ]
            tiles = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]
            
            def square(x, y):
                "Draw square using path at (x, y)."
                path.up()
                path.goto(x, y)
                path.down()
                path.begin_fill()
            
                for count in range(4):
                    path.forward(20)
                    path.left(90)
            
                path.end_fill()
            
            def offset(point):
                "Return offset of point in tiles."
                x = (floor(point.x, 20) + 200) / 20
                y = (180 - floor(point.y, 20)) / 20
                index = int(x + y * 20)
                return index
            
            def valid(point):
                "Return True if point is valid in tiles."
                index = offset(point)
            
                if tiles[index] == 0:
                    return False
            
                index = offset(point + 19)
            
                if tiles[index] == 0:
                    return False
            
                return point.x % 20 == 0 or point.y % 20 == 0
            
            def world():
                "Draw world using path."
                bgcolor('black')
                path.color('blue')
            
                for index in range(len(tiles)):
                    tile = tiles[index]
            
                    if tile > 0:
                        x = (index % 20) * 20 - 200
                        y = 180 - (index // 20) * 20
                        square(x, y)
            
                        if tile == 1:
                            path.up()
                            path.goto(x + 10, y + 10)
                            path.dot(2, 'white')
            
            def move():
                "Move pacman and all ghosts."
                writer.undo()
                writer.write(state['score'])
            
                clear()
            
                if valid(pacman + aim):
                    pacman.move(aim)
            
                index = offset(pacman)
            
                if tiles[index] == 1:
                    tiles[index] = 2
                    state['score'] += 1
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
            
                up()
                goto(pacman.x + 10, pacman.y + 10)
                dot(20, 'yellow')
            
                for point, course in ghosts:
                    if valid(point + course):
                        point.move(course)
                    else:
                        options = [
                            vector(5, 0),
                            vector(-5, 0),
                            vector(0, 5),
                            vector(0, -5),
                        ]
                        plan = choice(options)
                        course.x = plan.x
                        course.y = plan.y
            
                    up()
                    goto(point.x + 10, point.y + 10)
                    dot(20, 'red')
            
                update()
            
                for point, course in ghosts:
                    if abs(pacman - point) < 20:
                        return
            
                ontimer(move, 100)
            
            def change(x, y):
                "Change pacman aim if valid."
                if valid(pacman + vector(x, y)):
                    aim.x = x
                    aim.y = y
            
            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            writer.goto(160, 160)
            writer.color('white')
            writer.write(state['score'])
            listen()
            onkey(lambda: change(5, 0), 'Right')
            onkey(lambda: change(-5, 0), 'Left')
            onkey(lambda: change(0, 5), 'Up')
            onkey(lambda: change(0, -5), 'Down')
            world()
            move()
            done()
        elif gamechoice == 11:
            """Cannon, hitting targets with projectiles.
            
            Exercises
            
            1. Keep score by counting target hits.
            2. Vary the effect of gravity.
            3. Apply gravity to the targets.
            4. Change the speed of the ball.
            
            """
            
            from random import randrange
            from turtle import *
            from freegames import vector
            
            ball = vector(-200, -200)
            speed = vector(0, 0)
            targets = []
            
            def tap(x, y):
                "Respond to screen tap."
                if not inside(ball):
                    ball.x = -199
                    ball.y = -199
                    speed.x = (x + 200) / 25
                    speed.y = (y + 200) / 25
            
            def inside(xy):
                "Return True if xy within screen."
                return -200 < xy.x < 200 and -200 < xy.y < 200
            
            def draw():
                "Draw ball and targets."
                clear()
            
                for target in targets:
                    goto(target.x, target.y)
                    dot(20, 'blue')
            
                if inside(ball):
                    goto(ball.x, ball.y)
                    dot(6, 'red')
            
                update()
            
            def move():
                "Move ball and targets."
                if randrange(40) == 0:
                    y = randrange(-150, 150)
                    target = vector(200, y)
                    targets.append(target)
            
                for target in targets:
                    target.x -= 0.5
            
                if inside(ball):
                    speed.y -= 0.35
                    ball.move(speed)
            
                dupe = targets.copy()
                targets.clear()
            
                for target in dupe:
                    if abs(target - ball) > 13:
                        targets.append(target)
            
                draw()
            
                for target in targets:
                    if not inside(target):
                        return
            
                ontimer(move, 50)
            
            setup(420, 420, 370, 0)
            hideturtle()
            up()
            tracer(False)
            onscreenclick(tap)
            move()
            done()
        elif gamechoice == 12:
            """Flappy, game inspired by Flappy Bird.
            
            Exercises
            
            1. Keep score.
            2. Vary the speed.
            3. Vary the size of the balls.
            4. Allow the bird to move forward and back.
            
            """
            
            from random import *
            from turtle import *
            from freegames import vector
            
            bird = vector(0, 0)
            balls = []
            
            def tap(x, y):
                "Move bird up in response to screen tap."
                up = vector(0, 30)
                bird.move(up)
            
            def inside(point):
                "Return True if point on screen."
                return -200 < point.x < 200 and -200 < point.y < 200
            
            def draw(alive):
                "Draw screen objects."
                clear()
            
                goto(bird.x, bird.y)
            
                if alive:
                    dot(10, 'green')
                else:
                    dot(10, 'red')
            
                for ball in balls:
                    goto(ball.x, ball.y)
                    dot(20, 'black')
            
                update()
            
            def move():
                "Update object positions."
                bird.y -= 5
            
                for ball in balls:
                    ball.x -= 3
            
                if randrange(10) == 0:
                    y = randrange(-199, 199)
                    ball = vector(199, y)
                    balls.append(ball)
            
                while len(balls) > 0 and not inside(balls[0]):
                    balls.pop(0)
            
                if not inside(bird):
                    draw(False)
                    return
            
                for ball in balls:
                    if abs(ball - bird) < 15:
                        draw(False)
                        return
            
                draw(True)
                ontimer(move, 50)
            
            setup(420, 420, 370, 0)
            hideturtle()
            up()
            tracer(False)
            onscreenclick(tap)
            move()
            done()
ti.sleep(2)
shifoujixu = "1"
print("感谢您使用HugeMate智能！再见！\n\n")
ti.sleep(2)
sys.exit()