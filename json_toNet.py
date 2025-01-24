import json

def json_to_netscape(json_file, netscape_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            cookies = json.load(f)  # Đọc file JSON
        
        # Kiểm tra xem JSON có đúng định dạng hay không
        if isinstance(cookies, str):  # Nếu cookies là chuỗi, chuyển thành danh sách
            cookies = json.loads(cookies)
        elif not isinstance(cookies, list):
            raise ValueError("File JSON không đúng định dạng, cần danh sách các cookies.")

        with open(netscape_file, 'w', encoding='utf-8') as f:
            for cookie in cookies:
                domain = cookie.get("domain", "")
                host_only = "FALSE" if cookie.get("hostOnly") else "TRUE"
                path = cookie.get("path", "/")
                secure = "TRUE" if cookie.get("secure") else "FALSE"
                expiry = cookie.get("expirationDate", "0")
                name = cookie.get("name", "")
                value = cookie.get("value", "")
                f.write(f"{domain}\t{host_only}\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n")
        print(f"Chuyển đổi hoàn tất! File Netscape lưu tại: {netscape_file}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn tới file cookies JSON
json_file = "www.youtube.com_21-01-2025.json"  # Đặt tên file JSON của bạn
# Đường dẫn lưu file cookies Netscape
netscape_file = "cookies.txt"

json_to_netscape(json_file, netscape_file)