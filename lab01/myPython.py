#khai báo biến 
x=10 #Biến x lưu trữ giá trị số nguyên 10
name = "Thành Nam" #Biến name lưu trữ giá trị chuỗi "Thành Nam"
is_vaid = True #Biến is_vaid lưu trữ giá trị boolean True

# if =5 #Biến if không hợp lệ vì từ khóa "if" đã được sử dụng trong Python

#Các toán tử số học

#Phép cộng
a = 10
b = 3
result = a + b #Kết quả 13
#Phép trừ
a = 8
b = 4
result = a - b #Kết quả 4
#Phép nhân
a = 5
b = 2
result = a * b #Kết quả 10
#Phép chia
a = 10
b = 2
result = a / b #Kết quả 5.0
#Phép chia lấy nguyên
a = 10
b = 3
result = a // b #Kết quả 3
#Phép chia lấy dư
a = 10
b = 3
result = a % b #Kết quả 1
#Phép lũy thừa
a = 2
b = 3
result = a ** b #Kết quả 8


#Các toán tử logic
#Phép AND
x = 5
y = 3
result = (x > 2) and (y < 4) #Kết quả True
#Phép OR
x = 5
y = 3
result = (x > 2) or (y > 4) #Kết quả True
#Phép NOT
x = 5
result = not (x > 2) #Kết quả False
#Phép so sánh bằng 
x = 5
result = (x == 5) #Kết quả True
#Phép so sánh không bằng
x = 5
result = (x != 5) #Kết quả False
#Phép so sánh lớn hơn
x = 5
result = (x > 2) #Kết quả True
result = (x < 2) #Kết quả False
#Phép so sánh lớn hơn hoặc bằng
x = 5
result = (x >= 5) #Kết quả True
result = (x <= 3) #Kết quả False

#Nhập xuất dữ liệu
name = input("Nhập tên của bạn: ") #Nhập tên từ bàn phím
print("Xin chào, " + name) #In ra tên đã nhập
age = 25
print("Tuổi của bạn là: " + str(age)) #In ra tuổi đã nhập

print("Python", "là", "ngôn ngữ", "lập trình", sep= "-")
print("Xin chào", end= " ")
print("Các bạn")


#Các cấu trúc điều khiển
x=10
if x>5:
    print("x lớn hơn 5")
elif x==5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")
#Vòng lặp for
fruits = ["Táo", "Cam", "Chuối"]
for fruit in fruits:
    print(fruit) #In ra từng phần tử trong danh sách fruits
    
#Vòng lặp while
count = 0
while count < 5:
    print("Đếm đến", count)
    count += 1 #Tăng giá trị của biến count lên 1

#Câu lênh break
for i in range (1,101):
    if i%5==0:
        print("Số chia hết cho 5 đầu tiên là:", i)
        break
#Câu lệnh tiếp tục
for i in range(1, 11):
    if i == 5:
        continue #Bỏ qua số 5
    print(i) #In ra các số từ 1 đến 10, bỏ qua số 5
#Câu lệnh pass
for i in range(1, 11):
    if i == 5:
        pass #Không làm gì cả
    print(i) #In ra các số từ 1 đến 10, không bỏ qua số 5
    
#Chuỗi
#Khai báo chuỗi
#Sử dụng dấu ngoặc đơn
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn'
#Sử dụng dấu ngoặc kép
string_double_quotes = "Đây là một chuỗi sử dụng dấu ngoặc kép"
#Sử dụng dấu ngoặc ba,
string_triple_quotes = '''Đây là một chuỗi sử dụng dấu ngoặc ba
và có thể chứa nhiều dòng'''

#Truy cập ký tự trong chuỗi
my_string = "Python"
print(my_string[0]) #In ra ký tự đầu tiên trong chuỗi
print(my_string[1]) #In ra ký tự thứ hai trong chuỗi

#Các phép xử lý chuỗi trong python
my_string = "Hello, World!"
print(my_string[7:]) #In ra chuỗi từ vị trí 7 đến hết
print(my_string[:5]) #In ra chuỗi từ đầu đến vị trí 5
print(my_string[7:12]) #In ra chuỗi từ vị trí 7 đến 12
#Ghép chuỗi
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2 #Ghép hai chuỗi lại với nhau
#Độ dài chuỗi
my_string = "Python"
length = len(my_string) #Lấy độ dài của chuỗi

my_string = "   Hello, World!   "
print(my_string.strip()) #Xóa khoảng trắng ở đầu và cuối chuỗi
my_string = "Hello, World!"
print(my_string.split(","))
my_string = "Hello, World!"
print(my_string.replace("World", "Python")) #Thay thế "World" bằng "Python"

#Hàm(Function)
def greet(name):
    print("Xin chào, " + name) #Hàm greet in ra lời chào với tên đã nhập
    
def calculate_area(radius):
    area = 3.14 * radius ** 2 #Tính diện tích hình tròn
    return area #Trả về diện tích đã tính toán

def calculate_sum(a, b):
    return a + b #Hàm tính tổng hai số a và b
    return result
sum_result = calculate_sum(5, 10) #Gọi hàm calculate_sum với a=5 và b=10
print("Tổng là:", sum_result) #In ra kết quả tổng

#Mảng
from array import array
#Ví dụ:
from array import array
#Khai báo mảng số nguyên
int_array = array('i', [1, 2, 3, 4, 5])
#Khai báo mảng số thực
float_array = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(int_array[0]) #In ra phần tử đầu tiên của mảng số nguyên
print(float_array[1]) #In ra phần tử thứ hai của mảng số thực
int_array[0] = 10 #Thay đổi giá trị phần tử đầu tiên của mảng số nguyên
print(int_array[0]) #In ra giá trị đã thay đổi
int_array.append(6) #Thêm phần tử mới vào cuối mảng số nguyên
float_array.remove(2.2) #Xóa phần tử 2.2 khỏi mảng số thực
#Danh sách (list)
my_list = [1, 2, 3, 4, 5] #Khai báo danh sách số nguyên
names = ["Nam", "Hải", "Long"] #Khai báo danh sách chuỗi
mixed_list = [1, "Nam", 3.14, True] #Khai báo danh sách hỗn hợp
#Truy cập phần tử trong danh sách
print(my_list[0]) #In ra phần tử đầu tiên của danh sách
print(names[1]) #In ra phần tử thứ hai của danh sách
#Thay đổi giá trị phần tử trong danh sách
my_list[0] = 10 #Thay đổi giá trị phần tử đầu tiên của danh sách
print(my_list[0]) #In ra giá trị đã thay đổi
#Thêm phần tử vào danh sách
my_list.append(6) #Thêm phần tử 6 vào cuối danh sách
print(my_list) #In ra danh sách sau khi thêm phần tử
#Xóa phần tử khỏi danh sách
del my_list[0] #Xóa phần tử đầu tiên của danh sách
print(my_list) #In ra danh sách sau khi xóa phần tử
#Duyệt danh sách
for element in names:
    print(element) #In ra từng phần tử trong danh sách
    
#Kiểu Tuple
my_tuple = (1, 2, 3, 4, 5) #Khai báo tuple số nguyên
names = ("Nam", "Hải", "Long") #Khai báo tuple chuỗi
mixed_list = (1, "Nam", 3.14, True) #Khai báo tuple hỗn hợp
print(my_tuple[0]) #In ra phần tử đầu tiên của tuple
print(names[1]) #In ra phần tử thứ hai của tuple
#Đếm
my_tuple = (1, 2, 3, 4, 5, 1)
print(my_tuple.count(1)) #Đếm số lần xuất hiện của phần tử 1 trong tuple
#Tìm vị trí
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3)) #Tìm vị trí đầu tiên của phần tử 3 trong tuple 
#Khai báo dictionary
my_dict = {}
person = {"name": "Nam", "age": 25, "city": "Hà Nội"} #Khai báo dictionary với các cặp key-value
#Truy cập giá trị trong dictionary
print(person["name"]) #In ra giá trị của key "name"
print(person.get("age")) #In ra giá trị của key "age"
#Thêm cặp key-value vào dictionary
person["email"] ="nnam7485@gmail.com"
person["phone"] = "0123456789"
#Xóa cặp key-value khỏi dictionary
del person["city"] #Xóa cặp key-value với key "city"
age = person.pop("age") #Xóa cặp key-value với key "age" và lưu giá trị vào biến age

print(person.keys()) #In ra tất cả các key trong dictionary
print(person.values()) #In ra tất cả các giá trị trong dictionary
print(person.items()) #In ra tất cả các cặp key-value trong dictionary

#Lớp và đối tượng
class Car:
    def __init__(self, brand, model):
        self.brand = brand #Khởi tạo thuộc tính brand
        self.model = model #Khởi tạo thuộc tính model
    
    def get_info(self):
        return f"Car brand: {self.brand}, Model: {self.model}"
#Tạo đối tượng từ lớp Car
my_car = Car("Toyota", "Camry") #Tạo đối tượng my_car từ lớp Car
print(my_car.get_info()) #In ra thông tin của đối tượng my_car
#Thuộc tính Attribute
class Person:
    def __init__(self, name, age):
        self.name = name #Khởi tạo thuộc tính name
        self.age = age #Khởi tạo thuộc tính age
    class_name = "Người" #Thuộc tính lớp
#Truy cập thuộc tính
object_name = Person("Nam", 25) #Tạo đối tượng từ lớp Person
print(object_name.name) #In ra thuộc tính name của đối tượng
print(object_name.age) #In ra thuộc tính age của đối tượng
print(object_name.class_name) #In ra thuộc tính lớp class_name
#Phương thức Method
class ClassName:
    def method_name(self, parameter1, parameter2):
        #Thực hiện một số thao tác
        result = parameter1 + parameter2
        #Trả về kết quả
        return result
#Tạo đối tượng từ lớp ClassName
object_name = ClassName() #Tạo đối tượng từ lớp ClassName
#Gọi phương thức method_name
object_name.method_name(5, 10) #Gọi phương thức method_name với tham số 5 và 10
#Kế thừa
class ParentClass:
    def __init__(self, name):
        self.name = name #Khởi tạo thuộc tính name
class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name) #Gọi hàm khởi tạo của lớp cha
        self.age = age #Khởi tạo thuộc tính age
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
#Đa kế thừa
class Parent1:
    def method1(self):
        print("Phương thức từ lớp cha 1")
class Parent2:
    def method2(self):
        print("Phương thức từ lớp cha 2")
class Child(Parent1, Parent2):
    def method3(self):
        print("Phương thức từ lớp con")
#Đa hình
class Calculation:
    def add(self, a, b):
        return a + b #Phương thức cộng
    def subtract(self, a, b):
        return a - b #Phương thức trừ
class Animal:
    def sound(self):
        print("Động vật phát ra âm thanh")
class Dog(Animal):
    def sound(self):
        print("Chó sủa") #Phương thức phát ra âm thanh của chó

#Đa hình ở thời điểm chạy
class Animal:
    def make_sound(self):
        return "Động vật phát ra âm thanh"
class Dog(Animal):
    def make_sound(self):
        return "Chó sủa"
class Cat(Animal):
    def make_sound(self):
        return "Mèo kêu"
def animal_sound(animal):
    print(animal.make_sound()) #In ra âm thanh của động vật
dog = Dog() #Tạo đối tượng chó
cat = Cat() #Tạo đối tượng mèo
print(animal_sound(dog)) #Gọi hàm animal_sound với đối tượng chó
print(animal_sound(cat)) #Gọi hàm animal_sound với đối tượng mèo
#Trừu tượng hóa
from abc import ABC, abstractmethod
#lớp trừu tượng
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass #Phương thức trừu tượng không có thân hàm
class Dog(Animal):
    def make_sound(self):
        return "Chó sủa" #Phương thức cụ thể
class Cat(Animal):
    def make_sound(self):
        return "Mèo kêu" #Phương thức cụ thể
#Tạo đối tượng từ lớp Dog
dog = Dog() #Tạo đối tượng chó
cat = Cat() #Tạo đối tượng mèo
print(dog.make_sound()) #In ra âm thanh của chó
print(cat.make_sound()) #In ra âm thanh của mèo



