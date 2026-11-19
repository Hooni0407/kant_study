# shopping cart 클래스 선언
# 상품 목록 저장 기능
# 메서드
# - 장바구니 담기
# - 장바구니 빼기
# - 상품 목록 조회
class ShoppingCart:
    def __init__(self):
        self.bucket = []
    # - 장바구니 담기
    def add_item(self, item):
        self.bucket.append(item)
    # - 장바구니 빼기
    def remove_item(self, item):
        self.bucket.remove(item)
    # - 상품 목록 조회
    def show_items(self):
        return self.bucket
    


# 상품 클래스 
# 속성(변수, 인스턴스 변수)
# - 제품명
# - 가격
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 쇼핑 카트 생성
cart = ShoppingCart()

# 상품 3개 생성
item_a = Item("초코파이", 12_000)
item_b = Item("몽쉘", 12_000)
item_c = Item("대용량 팝콘", 12_000)

# 상품 1개 장바구니 담기
cart.add_item(item_a)

# 상품 1개 장바구니 담기
cart.add_item(item_b)

# 상품 1개 장바구니 담기
cart.add_item(item_c)

# 상품 1개 장바구니에서 빼기
cart.remove_item(item_b)

# 장바구니에 담김 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)



#====================================================================================================
# class ShoppingCart:
#     def __init__(self, product_list):
#         self.product_list = product_list
        
#     def ProductList(self):
#         self.product_list = []
    
#     def AddProduct(self):
#         self.product_list.append(self.product_list)
#         print(f"장바구니에 {self.product_name}이 담겼습니다.")

#     def RemoveProduct(self):
#         self.product_list.remove(self.product_list)
#         print(f"장바구니에 {self.product_list}이 삭제되었습니다.")


# class Product:
#     def __init__(self, product_name, price):
#         self.product_name = product_name
#         self.price = price

# product_1 = Product("hat", 20_000)
# product_2 = Product("jacket", 100_000)
# product_3 = Product("shoes", 150_000)
