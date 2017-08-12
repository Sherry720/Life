class Change():
    def _int_(self,number,db):
        self.number = number
        self.f = 0
        self.c = 0
        self.db = db
        self.binary_d = 0

    def numbers(self):      #返回了一个值就要用self，下同
        self.number = input("Enter your number:")
        self.number = float(self.number)
        return self.number

    def numbers_db(self):
        self.db =[]
        return self.db

    def numbers_f(self):
        x = input("小数点个数：")
        self.f = float( self.number % 1)      #小数部分
        self.f = round(float(self.number % 1),int(x))       #self.f是浮点数，这里小数部分四舍五入到实际位置
        
        return self.f

    def numbers_c(self):
        self.c = self.number - self.f
        self.c = int(self.c)      #整数部分
        return self.c

    
  
    def count(self):
        answer = input("你想进行那种换算：(十进制转换二进制输入：db，其余同理)\n")
        if answer == "db":    #十进制转换二进制
            binary_c = bin(self.c)
            binary_c = str(binary_c)
            while self.f != float(1):
                if self.f == 0:
                    break
                self.f = self.f * 2
                if self.f >= float(1):
                    self.db.append(1)
                    self.f -= float(1)
                else:
                    self.db.append(0)

            for x in self.db[:]:
                binary_c += str(x)

            binary_c = binary_c[2:]
            binary_c = int(binary_c)
            a = len(self.db)
            b = int(a)
            binary_d = binary_c / ( 10 ** b)
            print(binary_d)
        elif answer == 'do':
            binary_c = oct(self.c)
            binary_c = str(binary_c)
            while self.f != float(1):
                if self.f == 0:
                    break
                self.f = self.f *8
                if self.f >= float(1):
                    a = int(self.f)
                    self.db.append(a)
                    self.f -= a
                else:
                    self.db.append(0)

            for x in self.db[:]:
                binary_c += str(x)

            binary_c = binary_c[2:]
            binary_c = int(binary_c)
            a = len(self.db)
            b = int(a)
            binary_d = binary_c / ( 10 ** b)
            print(binary_d)
        else:
            return 0




change_0 = Change()
change_0.numbers()
change_0.numbers_db()
change_0.numbers_f()
change_0.numbers_c()
change_0.count()
