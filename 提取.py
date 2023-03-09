# encoding: utf-8
import os

WAN_ip = '172.19.83.1' #网关
IFC_ip = '172.19.83.237' #接口 
GAME = '测试游戏'
ipM24 = []
ipM16 = []

if os.path.exists(f"./{GAME}加速.txt"):
    exit(f'{GAME} file exist !!!')

with open ('./routes.txt') as f:
    lines = f.readlines()
    for i in lines:
        if WAN_ip  in i or IFC_ip in i:
            _ = i.strip().split() #按空格分割
            ip = _[0]
            MASK = sum([bin(int(j)).count('1') for j in _[1].split('.')]) #子网掩码
            if MASK >= 24:
                ipM24.append(ip+'/'+str(MASK) + '\n')
            else:
                ipM16.append(ip+'/'+str(MASK) + '\n')

with open (f'./{GAME}加速.txt','w') as f1:
    f1.write('小范围ip：只加速游戏服务器ip')
    f1.write('\n')
    f1.writelines(ipM24) #将ip/MASK 写入此文件

    f1.write('\n' * 10)

    f1.write('大范围ip：加速此ip可能会不稳定')
    f1.write('\n')
    f1.writelines(ipM16) #将ip/MASK 写入此文件

    
    

        