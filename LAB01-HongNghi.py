#1.2.3 Các toán tử số học

    #Cộng (+): Toán tử cộng được dùng để thực hiện phép cộng giữa hai số.
    a = 5
    b = 3
    result = a + b # Kết quả: 8

    #Trừ (-): Toán tử trừ được dùng để thực hiện phép trừ giữa hai số.
    a = 8
    b = 4
    result = a - b # Kết quả: 4

    #Nhân (*): Toán tử nhân được dùng để thực hiện phép nhân giữa hai số.
    a = 6
    b = 7
    result = a * b # Kết quả: 42

    #Chia (/): Toán tử chia được dùng để thực hiện phép chia.
    a = 20
    b = 5
    result = a / b # Kết quả: 4.0 (Kết quả luôn là một số thập phân nếu có phần dư)

    #Chia lấy phần nguyên (//): Toán tử chia lấy phần nguyên trả về kết quả là phần nguyên của phép chia.
    a = 20
    b = 3
    result = a // b # Kết quả: 6

    #Chia lấy dư (%): Toán tử này sẽ cung cấp phần còn lại sau khi thực hiện phép chia giữa hai số.
    a = 20
    b = 7
    remainder = a % b # Kết quả: 6 (Phần dư của 20 chia cho 7)

    #Lũy thừa ():** Toán tử lũy thừa được sử dụng để tính toán lũy thừa của một số.
    a = 2
    b = 3
    result = a ** b # Kết quả: 8 (2^3 = 8)

#1.2.4 Các toán tử logic

    #Phép toán AND: Toán tử "and" trả về "True" nếu cả hai điều kiện đều đúng.
    x = 5
    y = 3
    result = (x > 2) and (y < 4) # Kết quả: True

    #Phép toán OR: Toán tử "or" trả về "True" nếu ít nhất một trong hai điều kiện đầu vào là đúng.
    x = 5
    y = 3
    result = (x > 2) or (y > 4) # Kết quả: True

    #Phép toán NOT: Toán tử "not" trả về "True" nếu điều kiện là "False" và ngược lại.
    x = 5
    result = not (x == 5) # Kết quả: False

    #Phép so sánh bằng (==): Toán tử "==" sẽ so sánh hai giá trị có bằng nhau hay không.
    x = 5
    result = (x == 5) # Kết quả: True

    #Phép so sánh không bằng (!=): Toán tử "!=" sẽ so sánh hai giá trị có khác nhau hay không.
    x = 5
    result = (x != 3) # Kết quả: True

    #Phép so sánh lớn hơn (>), nhỏ hơn (<): Toán tử ">" sẽ so sánh xem giá trị bên trái lớn hơn giá trị bên phải hay không và toán tử "<" sẽ so sánh xem giá trị bên trái nhỏ hơn giá trị bên phải hay không.
    x = 5
    result1 = (x > 3) # Kết quả: True
    result2 = (x < 3) # Kết quả: False

    #Phép so sánh lớn hơn hoặc bằng (>=), nhỏ hơn hoặc bằng (<=): Toán tử ">=" sẽ so sánh xem giá trị bên trái lớn hơn hoặc bằng giá trị bên phải hay không và toán tử "<=" sẽ so sánh xem giá trị bên trái nhỏ hơn hoặc bằng giá trị bên phải hay không.
    x = 5
    result1 = (x >= 3) # Kết quả: True
    result2 = (x <= 3) # Kết quả: False

##1.2.5 Nhập, xuất dữ liệu

    #Hàm "input()" được dùng để nhập dữ liệu từ bàn phím. Nó cho phép nhập giá trị và trả về một chuỗi (string) biểu diễn giá trị đã nhập. Ta có thể lưu giá trị này vào biến để sử dụng sau này. Ví dụ:
    name = input("LeHongNghi: ")
    print("Xin chào, ", name)

    #Hàm "print()" được sử dụng để hiển thị dữ liệu ra màn hình hoặc console. Ta có thể truyền biến, chuỗi, hoặc giá trị cần hiển thị vào hàm "print()". 
    age = 22
    print("Tuổi của bạn là: ", age)

    print("Python", "là", "ngôn", "ngữ", "lập", "trình", sep="-") #Kết quả: Python-là-ngôn-ngữ-lập-trình

    print("Xin chào", end="")
    print("các bạn!") # Kết quả: Xin chào các bạn!

#1.2.6 Các cấu trúc điều khiển

    #Câu lệnh điều kiện (Conditional Statements): Cho phép kiểm tra điều kiện, thực hiện các khối mã khác nhau dựa trên kết quả của điều kiện. Ví dụ điển hình nhất trong Python là câu lệnh "if", "else", và "elif" (viết tắt của "else if"). Ví dụ:
    x = 10
    if x > 5:
    print("x lớn hơn 5")
    elif x == 5:
    print("x bằng 5")
    else:
    print("x nhỏ hơn 5")

    #Vòng lặp (Loops): Vòng lặp cho phép tự lặp lại việc thực hiện một khối mã cho đến khi một điều kiện nào đó được thỏa mãn. Trong Python, hai loại vòng lặp phổ biến nhất là vòng lặp "for" và "while".
    #Vòng lặp "for" được dùng để duyệt qua một chuỗi hoặc một tập hợp các phần tử. Ví dụ:
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
    print(fruit)
    #Vòng lặp "while" thực hiện việc lặp lại miễn khi điều kiện không còn đúng. Ví dụ:
    count = 0
    while count < 5:
    print(count)
    count += 1

    #Câu lệnh nhảy (Jump Statements): Câu lệnh nhảy được dùng để thay đổi luồng điều khiển của chương trình. Các câu lệnh nhảy phổ biến trong Python bao gồm "break", "continue" và "pass".
    #Sử dụng câu lệnh "break" để kết thúc một vòng lặp:
    #Tìm ra số chẵn hết cho 5 đầu tiên trong khoảng từ 1 đến 100
    for i in range(1, 101):
    if i % 5 == 0:
    print("Số chia hết cho 5 đầu tiên là:", i)
    break

    #Câu lệnh "continue" được dùng để bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang vòng lặp kế tiếp.
    #Tìm các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
    for i in range(1, 11):
    if i % 2 != 0:
    continue
    print(i)

    #Sử dụng câu lệnh "pass" chỉ là một tuyên bố rỗng:
    #Kiểm tra điều kiện, nếu đúng thực hiện, nếu sai thì không làm gì
    x = 5
    if x > 10:
    print("x lớn hơn 10")
    else:
    pass

#1.2.7 Chuỗi
    #Khai báo chuỗi trong Python:
    #Sử dụng dấu ngoặc đơn
    string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
    #Sử dụng dấu ngoặc kép
    string_double_quotes = "Đây là một chuỗi sử dụng dấu ngoặc kép."
    #Sử dụng dấu ngoặc ba
    string_triple_quotes = """Đây là một chuỗi
    có thể chứa nhiều dòng,
    có thể trải dài qua nhiều dòng."""

    #Truy cập ký tự trong chuỗi: Chúng ta có thể truy cập các ký tự trong chuỗi bằng cách sử dụng chỉ số của chúng trong cặp dấu ngoặc vuông []. Chuỗi ý rằng chỉ số trong Python bắt đầu từ 0. Ví dụ:
    my_string = "Hello, World!"
    print(my_string[0]) # Kết quả: 'H'
    print(my_string[7]) # Kết quả: 'W'

    #Các phép xử lý chuỗi trong Python:
    #Cắt chuỗi (Slicing): Cắt chuỗi là quá trình lấy một phần của chuỗi sử dụng chỉ mục hoặc phạm vi chỉ mục.
    my_string = "Hello, World!"
    print(my_string[0:5]) # Lấy từ ký tự thứ 0 đến hết ký tự thứ 5: Kết quả: 'Hello'
    print(my_string[7:]) # Lấy từ dấu đến ký tự thứ 7: Kết quả: 'World!'
    print(my_string[3:8]) # Lấy từ ký tự thứ 3 đến ký tự thứ 7: Kết quả: 'lo, W'
    #Ghép chuỗi (Concatenation): Ghép chuỗi là quá trình nối chuỗi lại với nhau.
    string1 = "Hello"
    string2 = "World"
    concatenated_string = string1 + " " + string2 # Kết quả: 'Hello World'
    #Độ dài chuỗi (Length): Hàm "len()" được dùng để tính độ dài của chuỗi.
    my_string = "Hello, World!"
    length = len(my_string) # Kết quả: 13

    # Một số hàm dùng để xử lý các chuỗi trong Python:
    # ".upper()": Chuyển đổi chuỗi thành chữ hoa.
    # ".lower()": Chuyển đổi chuỗi thành chữ thường.
    # ".strip()": Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
    # ".split()": Phân tách chuỗi thành danh sách các từ hoặc phần tử.
    # ".replace()": Thay thế một phần của chuỗi bằng một chuỗi khác.
    my_string = " Hello, World! "
    print(my_string.strip()) # Loại bỏ khoảng trắng: Kết quả: 'Hello, World!'
    my_string = "Hello, World!"
    print(my_string.split(',')) #Phân tách chuỗi: Kết quả: ['Hello', ' World!']
    my_string = "Hello, World!"
    print(my_string.replace("Hello", "Hi")) #Thay thế chuỗi. Kết quả: Hi, World!

#1.2.8 Hàm (Function)

    #Khai báo hàm: Để định nghĩa một hàm trong Python, ta sử dụng từ khóa "def", tiếp theo là tên hàm và danh sách tham số (nếu có), sau đó là một khối mã được thụt lề bên trong dấu hai chấm.
    def my_function(parameter1, parameter2):
    #Khối mã của hàm
    #Thực hiện các hoạt động dựa trên tham số được truyền vào
    result = parameter1 + parameter2
    return result

    #Gọi hàm: Để sử dụng hàm, chỉ cần gọi tên hàm cùng với các đối số cần thiết (nếu có). Ví dụ:
    result = my_function(10, 20) # Gọi hàm và lưu kết quả vào biến result
    print(result) # In kết quả của hàm

    #Ví dụ về khai báo và gọi hàm trong Python:
    #Định nghĩa hàm tính tổng
    def calculate_sum(a, b):
    result = a + b
    return result
    #Gọi hàm và lưu kết quả vào biến
    sum_result = calculate_sum(10, 20)
    #In kết quả
    print("Tổng hai số là:", sum_result)

    #Ví dụ khai báo và gọi hàm không có giá trị trả về:
    #Hàm không trả về giá trị, chỉ in ra thông báo
    def greet(name):
    print("Xin chào, ", name)
    #Gọi hàm
    greet("Alice")

#1.3.1 KIỂU DỮ LIỆU CÓ CẤU TRÚC

    #Để sử dụng mảng trong Python, chúng ta cần import module "array":
    from array import array

    #Khai báo mảng trong module "array": Có hai tham số quan trọng khi khai báo một mảng:
    #Typecode: Đây là một ký tự xác định kiểu dữ liệu của các phần tử trong mảng.
    #Initializer: Đây là danh sách các giá trị ban đầu của mảng.
    #Ví dụ:
    from array import array
    #Khai báo một mảng số nguyên
    int_array = array('i', [1, 2, 3, 4, 5])
    #Khai báo một mảng số thực
    float_array = array('f', [3.14, 2.5, 6.7])

    #Phương thức và thuộc tính của mảng:
    #Truy cập phần tử trong mảng: Truy cập các phần tử trong mảng bằng cách sử dụng chỉ số của chúng.
    print(int_array[0]) # Truy cập phần tử đầu tiên của mảng số nguyên
    print(float_array[2]) # Truy cập phần tử thứ ba của mảng số thực
    #Cập nhật giá trị của phần tử trong mảng:
    int_array[2] = 10 #Cập nhật giá trị của phần tử thứ ba trong mảng số nguyên

    #Sử dụng các phương thức của mảng: Module “array” cung cấp một số phương thức để thực hiện các thao tác với mảng:
    int_array.append(6) # Thêm phần tử 6 vào cuối mảng số nguyên
    float_array.remove(6.7) # Xóa phần tử 6.7 khỏi mảng số thực

#1.3.2 Danh sách (List)

    #Khai báo một danh sách (List):
    #Danh sách số nguyên
    my_list = [1, 2, 3, 4, 5]
    #Danh sách chuỗi
    names = ["Alice", "Bob", "Charlie"]
    #Danh sách kết hợp kiểu dữ liệu
    mixed_list = [10, "hello", 3.14, True]

    #Cách sử dụng danh sách:
    #Truy cập vào một phần tử ở trong danh sách:
    print(my_list[0]) # Truy cập phần tử đầu tiên: Kết quả: 1
    print(names[2]) # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

    #Cập nhật giá trị của một phần tử ở trong danh sách:
    my_list[1] = 20 # Thay đổi giá trị của phần tử thứ hai
    print(my_list) # Kết quả: [1, 20, 3, 4, 5]

    #Thêm một phần tử vào danh sách:
    names.append("David") # Thêm phần tử vào cuối danh sách
    print(names) # Kết quả: ['Alice', 'Bob', 'Charlie', 'David']

    #Xóa một phần tử khỏi danh sách:
    del my_list[2] # Xóa phần tử thứ ba khỏi danh sách
    print(my_list) # Kết quả: [1, 20, 4, 5]

    #Duyệt qua từng phần tử trong danh sách:
    for element in names:
    print(element) # In từng phần tử trong danh sách

#1.3.3 Kiểu Tuple

    #Khai báo Tuple: Có thể báo một tuple bằng cách sử dụng dấu ngoặc đơn và phân tách các phần tử bằng dấu phẩy. Ví dụ:
    #Tuple các số nguyên
    my_tuple = (1, 2, 3, 4, 5)
    #Tuple các chuỗi
    names = ("Alice", "Bob", "Charlie")
    #Tuple kết hợp kiểu dữ liệu
    mixed_tuple = (10, "hello", 3.14)

    #Truy cập vào phần tử trong Tuple: Tương tự như danh sách, có thể truy cập các phần tử trong Tuple bằng cách sử dụng chỉ số của chúng. Ví dụ:
    print(my_tuple[0]) # Truy cập phần tử đầu tiên: Kết quả: 1
    print(names[2]) # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

    #Các phương thức trong Tuple:
    #count(value): Đếm số lần một giá trị cụ thể trong tuple xuất hiện. Ví dụ:
    my_tuple = (1, 2, 3, 1, 4, 1)
    print(my_tuple.count(1)) # Kết quả: 3 (1 xuất hiện 3 lần trong tuple)

    #index(value): Trả về chỉ số đầu tiên của một giá trị cụ thể trong tuple. Ví dụ:
    my_tuple = ('a', 'b', 'c', 'd', 'b')
    print(my_tuple.index('b')) #Kết quả: 1 (chỉ số đầu tiên của 'b' trong tuple là 1)

#1.3.4 Kiểu Dictionary

    #- Khai báo dictionary:
    # Khai bảo một dictionary rỗng
    my_dict = {}
    # Khai báo một dictionary với các cặp key-value
    person = {"name": "Alice", "age": 25, "city": "New York"}

    #Truy cập vào giá trị trong dictionary:
    #Có thể truy cập giá trị trong dictionary bằng cách sử dụng key tương ứng, ví dụ:
    print(person["name"]) # In giá trị của key "name": Kết quả: "Alice"
    print(person["age"]) # In giá trị của key "age": Kết quả: 25

    #Thêm hoặc cập nhật giá trị trong dictionary:
    # Thêm một cặp key-value mới
    person["email"] = "alice@example.com"
    # Cập nhật giá trị của key đã tồn tại
    person["age"] = 26

    #Xóa một phần tử trong dictionary:
    # Xóa một cập koy-value từ dictionary
    del person["city"]
    # Xóa phần từ và lấy giá trị của key
    age - person.pop("age")

    #Các phương thức và phương thức dành cho dictionary:
    # "keys()": Trả về tất cả các keys trong dictionary.
    # "values()": Trà về tất cả các values trong dictionary.
    # "items()": Trả về tất cả các cặp key-value trong dictionary dưới dạng tuple.
    #Ví dụ:
    print(person.keys()) # In ra tất cả các keys trong dictionary
    print(person.values()) # In ra tất cả các values trong dictionary
    print(person.items()) # In ra tất cả các cặp key-value trong dictionary
