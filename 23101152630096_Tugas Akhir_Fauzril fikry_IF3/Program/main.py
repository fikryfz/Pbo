from models.customer import Customer_fikry
from models.product import Product_fikry
from models.motorcycle import MotorCycle_fikry
from models.electric_motorcycle import ElectricMotorCycle_fikry
from models.order import Order_fikry
import mysql.connector # type: ignore
from datetime import datetime, timedelta
import time  
from colorama import Fore, Style  
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_motor_fikry"
)

cursor = db.cursor()

def rgb_text(text, r, g, b):
    """Fungsi untuk mengubah teks menjadi warna RGB."""
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def animate_exit_message(message):
    for char in message:

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        colored_char = rgb_text(char, r, g, b)  
        print(colored_char, end='', flush=True) 
        time.sleep(0.1)  
    print()  

def animate_opening_message(message):
    for i in range(len(message) + 1):
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        colored_message = rgb_text(message[:i], r, g, b) 
        print('\r' + ' ' * (len(message) - i) + colored_message, end='', flush=True)  
        time.sleep(0.1)  
    print()  

def main():
    while True:
        print("\n=== SISTEM MANAJEMEN TOKO MOTOR ===")
        print("1. Kelola Customer")
        print("2. Kelola Produk")
        print("3. Kelola Order")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            menu_customer()
        elif pilihan == "2":
            menu_product()
        elif pilihan == "3":
            menu_order()
        elif pilihan == "4":
            animate_exit_message("Sampai jumpa dan terima kasih!,Salam Hangat Dari Toko Motor Fikry:)")  

        else:
            print("Pilihan tidak valid!")

def menu_customer():
    while True:
        print("\n=== MENU CUSTOMER ===")
        print("1. Tambah Customer")
        print("2. Update Customer")
        print("3. Hapus Customer")
        print("4. Tampilkan Customer")
        print("5. Kembali")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            cust_id = input("Masukkan ID Customer: ")
            cursor.execute("SELECT * FROM customers_fikry WHERE cust_id = %s", (cust_id,))
            if cursor.fetchone():
                print("ID Customer sudah digunakan!")
                continue
                
            cust_name = input("Masukkan Nama Customer: ")
            sql = "INSERT INTO customers_fikry (cust_id, cust_name) VALUES (%s, %s)"
            val = (cust_id, cust_name)
            cursor.execute(sql, val)
            db.commit()
            print("Customer berhasil ditambahkan!")
            
        elif pilihan == "2":
            cursor.execute("SELECT * FROM customers_fikry")
            customers = cursor.fetchall()
            if not customers:
                print("Belum ada customer!")
                continue
                
            print("\nDaftar Customer yang ada:")
            Customer_fikry.header_fikry()
            for customer in customers:
                print("|{:^8}|{:^25}|".format(customer[0], customer[1]))
            print("+"+"-"*8+"+"+"-"*25+"+")
                
            cust_id = input("\nMasukkan ID Customer yang akan diupdate: ")
            new_name = input("Masukkan Nama Baru: ")
            
            sql = "UPDATE customers_fikry SET cust_name = %s WHERE cust_id = %s"
            val = (new_name, cust_id)
            cursor.execute(sql, val)
            db.commit()
            
            if cursor.rowcount > 0:
                print("Customer berhasil diupdate!")
            else:
                print("Customer tidak ditemukan!")

        elif pilihan == "3":
            cursor.execute("SELECT * FROM customers_fikry")
            customers = cursor.fetchall()
            if not customers:
                print("Belum ada customer!")
                continue
                
            print("\nDaftar Customer yang ada:")
            Customer_fikry.header_fikry()
            for customer in customers:
                print("|{:^8}|{:^25}|".format(customer[0], customer[1]))
            print("+"+"-"*8+"+"+"-"*25+"+")
                
            cust_id = input("\nMasukkan ID Customer yang akan dihapus: ")
            
            sql = "DELETE FROM customers_fikry WHERE cust_id = %s"
            val = (cust_id,)
            cursor.execute(sql, val)
            db.commit()
            
            if cursor.rowcount > 0:
                print("Customer berhasil dihapus!")
            else:
                print("Customer tidak ditemukan!")
                
        elif pilihan == "4":
            cursor.execute("SELECT * FROM customers_fikry")
            customers = cursor.fetchall()
            if customers:
                print("\nDaftar Customer:")
                Customer_fikry.header_fikry()
                for customer in customers:
                    print("|{:^8}|{:^25}|".format(customer[0], customer[1]))
                print("+"+"-"*8+"+"+"-"*25+"+")
            else:
                print("Belum ada customer!")
                
        elif pilihan == "5":
            break

def menu_product():
    while True:
        print("\n=== MENU PRODUK ===")
        print("1. Tambah Produk")
        print("2. Update Produk")
        print("3. Hapus Produk")
        print("4. Tampilkan Produk")
        print("5. Kembali")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            print("\nJenis Produk:")
            print("1. Motor Biasa")
            print("2. Motor Listrik")
            jenis = input("Pilih jenis produk (1/2): ")
            
            id_product = input("Masukkan ID Produk: ")
            name = input("Masukkan Nama Produk: ")
            price = float(input("Masukkan Harga: "))
            
            if jenis == "1":
                cylinder = int(input("Masukkan Cylinder (CC): "))
                tank_capacity = float(input("Masukkan Kapasitas Tangki (L): "))
                battery = None
                mileage = None
                product_type = 'motorcycle'
            else:
                cylinder = None
                tank_capacity = None
                battery = input("Masukkan Kapasitas Baterai (kWh): ")
                mileage = float(input("Masukkan Jarak Tempuh (km): "))
                product_type = 'electric'
            
            sql = "INSERT INTO products_fikry (id_product, name, price, product_type, cylinder, tank_capacity, battery, mileage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id_product, name, price, product_type, cylinder, tank_capacity, battery, mileage)
            cursor.execute(sql, val)
            db.commit()
            print("Produk berhasil ditambahkan!")
            
        elif pilihan == "2":
            cursor.execute("SELECT * FROM products_fikry")
            products = cursor.fetchall()
            if not products:
                print("Belum ada produk!")
                continue
                
            print("\nDaftar Produk yang ada:")
            Product_fikry.header_fikry()
            for product in products:
                try:
                    if product[3] == 'motorcycle':
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),  
                            str(product[1] or ''),  
                            f"Rp{float(product[2] or 0):,.0f}",  
                            f"{str(product[4] or '-')} CC",  
                            f"{str(product[5] or '-')}L",  
                            "Motor Biasa"
                        ))
                    else:  # electric
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),  
                            str(product[1] or ''),  
                            f"Rp{float(product[2] or 0):,.0f}",  
                            f"{str(product[6] or '-')}kWh",  
                            f"{str(product[7] or '-')}km",   
                            "Motor Listrik"
                        ))
                except (TypeError, ValueError) as e:
                    continue
            print("+" + "-"*8 + "+" + "-"*25 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")
                
            id_product = input("\nMasukkan ID Produk yang akan diupdate: ")
            cursor.execute("SELECT * FROM products_fikry WHERE id_product = %s", (id_product,))
            product = cursor.fetchone()
            
            if product:
                product_type = product[3]
                if product_type == "motorcycle":
                    new_name = input("Masukkan Nama Baru: ")
                    new_price = float(input("Masukkan Harga Baru: "))
                    new_cylinder = int(input("Masukkan Cylinder Baru (CC): "))
                    new_tank_capacity = float(input("Masukkan Kapasitas Tangki Baru (L): "))
                    sql = "UPDATE products_fikry SET name = %s, price = %s, cylinder = %s, tank_capacity = %s WHERE id_product = %s"
                    val = (new_name, new_price, new_cylinder, new_tank_capacity, id_product)
                else:  # electric
                    new_name = input("Masukkan Nama Baru: ")
                    new_price = float(input("Masukkan Harga Baru: "))
                    new_battery = input("Masukkan Kapasitas Baterai Baru (kWh): ")
                    new_mileage = float(input("Masukkan Jarak Tempuh Baru (km): "))
                    sql = "UPDATE products_fikry SET name = %s, price = %s, battery = %s, mileage = %s WHERE id_product = %s"
                    val = (new_name, new_price, new_battery, new_mileage, id_product)
                
                cursor.execute(sql, val)
                db.commit()
                print("Produk berhasil diupdate!")
                
                
                cursor.execute("SELECT * FROM products_fikry WHERE id_product = %s", (id_product,))
                updated_product = cursor.fetchone()
                print("\nData Produk Setelah Update:")
                Product_fikry.header_fikry()
                if product_type == "motorcycle":
                    print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                        str(updated_product[0]),
                        str(updated_product[1]),
                        f"Rp{float(updated_product[2]):,.0f}",
                        f"{str(updated_product[4])} CC",
                        f"{str(updated_product[5])}L",
                        "Motor Biasa"
                    ))
                else:
                    print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                        str(updated_product[0]),
                        str(updated_product[1]),
                        f"Rp{float(updated_product[2]):,.0f}",
                        f"{str(updated_product[6])}kWh",
                        f"{str(updated_product[7])}km",
                        "Motor Listrik"
                    ))
                print("+" + "-"*8 + "+" + "-"*25 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")
            else:
                print("Produk tidak ditemukan!")
                
        elif pilihan == "3":
            cursor.execute("SELECT * FROM products_fikry")
            products = cursor.fetchall()
            if not products:
                print("Belum ada produk!")
                continue
                
            print("\nDaftar Produk:")
            Product_fikry.header_fikry()
            for product in products:
                try:
                    if product[3] == 'motorcycle':
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),
                            str(product[1] or ''),
                            f"Rp{float(product[2] or 0):,.0f}",
                            f"{str(product[4] or '-')} CC",
                            f"{str(product[5] or '-')}L",
                            "Motor Biasa"
                        ))
                    else: 
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),
                            str(product[1] or ''),
                            f"Rp{float(product[2] or 0):,.0f}",
                            f"{str(product[6] or '-')}kWh",
                            f"{str(product[7] or '-')}km",
                            "Motor Listrik"
                        ))
                except (TypeError, ValueError) as e:
                    continue
            print("+" + "-"*8 + "+" + "-"*25 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")
            
            id_product = input("Masukkan ID Produk yang akan dihapus: ")
            
            
            cursor.execute("SELECT COUNT(*) FROM orders_fikry WHERE id_product = %s", (id_product,))
            order_count = cursor.fetchone()[0]
            
            if order_count > 0:
                print(f"Tidak dapat menghapus produk karena masih digunakan dalam {order_count} order!")
                print("Hapus order terkait terlebih dahulu.")
                continue
            
            cursor.execute("SELECT * FROM products_fikry WHERE id_product = %s", (id_product,))
            product = cursor.fetchone()
            if product:
                try:
                    sql = "DELETE FROM products_fikry WHERE id_product = %s"
                    cursor.execute(sql, (id_product,))
                    db.commit()
                    print("Produk berhasil dihapus!")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    print("Gagal menghapus produk!")
            else:
                print("Produk tidak ditemukan!")
                
        elif pilihan == "4":
            cursor.execute("SELECT * FROM products_fikry")
            products = cursor.fetchall()
            if products:
                print("\nDaftar Produk:")
                Product_fikry.header_fikry()
                for product in products:
                    try:
                        if product[3] == 'motorcycle':
                            print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                                str(product[0] or ''), 
                                str(product[1] or ''),
                                f"Rp{float(product[2] or 0):,.0f}", 
                                f"{str(product[4] or '-')} CC", 
                                f"{str(product[5] or '-')}L",  
                                "Motor Biasa"
                            ))
                        else:  # electric
                            print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                                str(product[0] or ''),  
                                str(product[1] or ''),  
                                f"Rp{float(product[2] or 0):,.0f}",  
                                f"{str(product[6] or '-')}kWh",  
                                f"{str(product[7] or '-')}km",  
                                "Motor Listrik"
                            ))
                    except (TypeError, ValueError) as e:
                        continue  
                print("+" + "-"*8 + "+" + "-"*25 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")
            else:
                print("Belum ada produk!")
                
        elif pilihan == "5":
            break

def menu_order():
    while True:
        print("\n=== MENU ORDER ===")
        print("1. Buat Order")
        print("2. Hapus Order")
        print("3. Tampilkan Order")
        print("4. Detail Order")
        print("5. Kembali")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            cursor.execute("SELECT * FROM customers_fikry")
            customers = cursor.fetchall()
            if not customers:
                print("Pastikan ada customer terlebih dahulu!")
                continue
                
            print("\nDaftar Customer:")
            Customer_fikry.header_fikry()
            for customer in customers:
                print("|{:^8}|{:^25}|".format(customer[0], customer[1]))
            print("+"+"-"*8+"+"+"-"*25+"+")
            cust_id = input("\nMasukkan ID Customer: ")
            
            cursor.execute("SELECT * FROM products_fikry")
            products = cursor.fetchall()
            if not products:
                print("Pastikan ada produk terlebih dahulu!")
                continue
                
            print("\nDaftar Produk:")
            Product_fikry.header_fikry()
            for product in products:
                try:
                    if product[3] == 'motorcycle':
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),
                            str(product[1] or ''),
                            f"Rp{float(product[2] or 0):,.0f}",
                            f"{str(product[4] or '-')} CC",
                            f"{str(product[5] or '-')}L",
                            "Motor Biasa"
                        ))
                    else:  
                        print("|{:^8}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
                            str(product[0] or ''),
                            str(product[1] or ''),
                            f"Rp{float(product[2] or 0):,.0f}",
                            f"{str(product[6] or '-')}kWh",
                            f"{str(product[7] or '-')}km",
                            "Motor Listrik"
                        ))
                except (TypeError, ValueError) as e:
                    continue
            print("+" + "-"*8 + "+" + "-"*25 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+" + "-"*15 + "+")
            prod_id = input("\nMasukkan ID Produk: ")
            
            
            try:
                cust_id = int(cust_id)
                prod_id = int(prod_id)
                
                
                cursor.execute("SELECT * FROM customers_fikry WHERE cust_id = %s", (cust_id,))
                selected_customer = cursor.fetchone()
                
                cursor.execute("SELECT * FROM products_fikry WHERE id_product = %s", (prod_id,))
                selected_product = cursor.fetchone()
                
                if selected_customer and selected_product:
                    quantity = int(input("Masukkan Jumlah: "))
                    cursor.execute("SELECT MAX(id_order) FROM orders_fikry")
                    last_id = cursor.fetchone()[0]
                    order_id = 1 if last_id is None else last_id + 1
                    
                    total = float(selected_product[2]) * quantity
                    
                    print("\nDetail Order yang akan dibuat:")
                    print("\n+" + "-"*60 + "+")
                    print("|{:^60}|".format("DETAIL ORDER"))
                    print("+" + "-"*60 + "+")
                    print("|{:<25}: {:<32}|".format("ID Order", order_id))
                    print("|{:<25}: {:<32}|".format("Tanggal", datetime.now().strftime("%Y-%m-%d %H:%M")))
                    print("|{:<25}: {:<32}|".format("ID Customer", selected_customer[0]))
                    print("|{:<25}: {:<32}|".format("Nama Customer", selected_customer[1]))
                    print("|{:<25}: {:<32}|".format("ID Produk", selected_product[0]))
                    print("|{:<25}: {:<32}|".format("Nama Produk", selected_product[1]))
                    print("|{:<25}: Rp{:<30,.0f}|".format("Harga", float(selected_product[2])))
                    print("|{:<25}: {:<32}|".format("Quantity", quantity))
                    print("|{:<25}: Rp{:<30,.0f}|".format("Total", total))
                    print("+" + "-"*60 + "+")
                    
                    confirm = input("\nKonfirmasi pembuatan order (y/n)? ").lower()
                    if confirm == 'y':
                        sql = "INSERT INTO orders_fikry (id_order, cust_id, id_product, order_date, quantity, total) VALUES (%s, %s, %s, %s, %s, %s)"
                        val = (order_id, selected_customer[0], selected_product[0], datetime.now(), quantity, total)
                        cursor.execute(sql, val)
                        db.commit()
                        print("Order berhasil dibuat!")
                    else:
                        print("Pembuatan order dibatalkan!")
                else:
                    print("Customer atau Produk tidak ditemukan!")
            except ValueError:
                print("ID harus berupa angka!")
                
        elif pilihan == "2":
            order_id = input("Masukkan ID Order yang akan dihapus: ")
            cursor.execute("SELECT * FROM orders_fikry WHERE id_order = %s", (order_id,))
            order = cursor.fetchone()
            if order:
                sql = "DELETE FROM orders_fikry WHERE id_order = %s"
                cursor.execute(sql, (order_id,))
                db.commit()
                print("Order berhasil dihapus!")
            else:
                print("Order tidak ditemukan!")
                
        elif pilihan == "3":
            cursor.execute("""
                SELECT o.id_order, o.cust_id, o.order_date 
                FROM orders_fikry o 
                ORDER BY o.order_date DESC
            """)
            orders = cursor.fetchall()
            if orders:
                print("\nDaftar Order:")
                Order_fikry.header_fikry()
                for order in orders:
                    formatted_date = order[2].strftime("%Y-%m-%d")  
                    print("|{:^8}|{:^15}|{:^20}|".format(
                        order[0],         
                        order[1],         
                        formatted_date    
                    ))
                print("+" + "-"*8 + "+" + "-"*15 + "+" + "-"*20 + "+")
            else:
                print("Belum ada order!")
                
        elif pilihan == "4":
            order_id = input("Masukkan ID Order: ")
            cursor.execute("""
                SELECT o.*, c.cust_name, p.name as product_name, p.price 
                FROM orders_fikry o
                JOIN customers_fikry c ON o.cust_id = c.cust_id
                JOIN products_fikry p ON o.id_product = p.id_product
                WHERE o.id_order = %s
            """, (order_id,))
            order = cursor.fetchone()
            if order:
                print("\n+" + "-"*60 + "+")
                print("|{:^60}|".format("DETAIL ORDER"))
                print("+" + "-"*60 + "+")
                print("|{:<25}: {:<32}|".format("ID Order", order[0]))
                print("|{:<25}: {:<32}|".format("Tanggal", order[3].strftime("%Y-%m-%d %H:%M")))
                print("|{:<25}: {:<32}|".format("ID Customer", order[1]))
                print("|{:<25}: {:<32}|".format("Nama Customer", order[6]))
                print("|{:<25}: {:<32}|".format("ID Produk", order[2]))
                print("|{:<25}: {:<32}|".format("Nama Produk", order[7]))
                print("|{:<25}: Rp{:<30,.0f}|".format("Harga", float(order[8])))
                print("|{:<25}: {:<32}|".format("Quantity", order[4]))
                print("|{:<25}: Rp{:<30,.0f}|".format("Total", float(order[5])))
                print("+" + "-"*60 + "+")
            else:
                print("Order tidak ditemukan!")
                
        elif pilihan == "5":
            break

if __name__ == "__main__":
    animate_opening_message("Selamat datang di Sistem Manajemen Toko Motor Fikry!")  
    main() 