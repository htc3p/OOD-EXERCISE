'''
น้องมีเงิน m บาท ช็อกโกแลตราคา p บาท ร้านค้ามีนโยบายว่าสามารถนำที่ห่อช็อกโกแลต w แผ่น
จงหาว่าน้องสามารถกินช็อกโกแลตสูงสุดได้กี่ชิ้น

Input: money = 16, price = 2, wrap = 2
Output:   15
ตอนแรกมีเงิน 16 บาท ช็อกโกแลตราคา 2 บาท ก็จะสามารถซื้อได้ 8 ชิ้น นำที่ห่อช็อกโกแลต 8 แผ่นมาแลกช็อกโกแลตได้อีก 4 ชิ้นแล้วก็นำที่ห่อช็อกโกแลต 4 แผ่นมาแลกช็อกโกแลตได้ 2 ชิ้น สุดท้ายก็นำที่ห่อช็อกโกแลต 2 แผ่นมาแลกช็อกโกแลต 1 ชิ้น
8 + 4 + 2 + 1 = 15
'''


money, price, wrap = map(int, input('Enter m, p, w: ').split())
buy = money // price
def calculate_wrapper(buy, wrap):
    if buy < wrap:
        return buy
    else:
        remaining_wraps = buy % wrap
        total_wraps = buy + calculate_wrapper((buy + remaining_wraps)//wrap , wrap)
        return total_wraps

print(calculate_wrapper(buy, wrap))