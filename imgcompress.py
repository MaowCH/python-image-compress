from PIL import Image
from tkinter import Tk, filedialog
import os

def convert_to_jpg(input_path, output_folder):
    try:
        with Image.open(input_path) as img:
            # สร้างโฟลเดอร์ "min" หากยังไม่มี
            os.makedirs(output_folder, exist_ok=True)

            # สร้างชื่อไฟล์ที่แปลงจาก PNG เป็น JPEG
            jpg_output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_path))[0]}.jpg")

            # แปลง PNG เป็น JPEG
            img.convert("RGB").save(jpg_output_path, 'JPEG', quality=60)
            print(f'ไฟล์ PNG แปลงเป็น JPEG: {input_path} -> {jpg_output_path}')
            
            return jpg_output_path
    except Exception as e:
        print(f'เกิดข้อผิดพลาดในการแปลง: {e}')
        return None

def reduce_image_size(input_path, output_folder, max_size_kb=100, quality=60):
    try:
        with Image.open(input_path) as img:
            # คำนวณขนาดไฟล์ JPEG ที่ลดลง
            target_size_kb = max_size_kb * 0.9  # ให้เล็กลงเล็กน้อยกว่า 100KB เพื่อป้องกันการเกิน
            current_size_kb = os.path.getsize(input_path) / 1024

            # หาค่า scale factor เพื่อลดขนาดไฟล์
            scale_factor = (target_size_kb / current_size_kb) ** 0.5

            # สร้างโฟลเดอร์ "min" หากยังไม่มี
            os.makedirs(output_folder, exist_ok=True)

            # สร้างชื่อไฟล์ลดขนาดลง
            output_path = os.path.join(output_folder, f"reduced_{os.path.basename(input_path)}")

            # ลดคุณภาพและบันทึกรูปภาพ (คงที่ขนาดความกว้างและความสูง)
            img.save(output_path, 'JPEG', quality=quality)
            print(f'ขนาดไฟล์ลดลง: {input_path} -> {output_path}')
    except Exception as e:
        print(f'เกิดข้อผิดพลาด: {e}')

def select_files():
    root = Tk()
    root.withdraw()  # ซ่อนหน้าต่างหลัก

    # เลือกไฟล์หลาย ๆ รูปภาพ
    file_paths = filedialog.askopenfilenames(
        title='เลือกไฟล์รูปภาพ',
        filetypes=[('JPEG files', '*.jpg;*.jpeg'), ('PNG files', '*.png'), ('All files', '*.*')]
    )

    # ตัวอย่างการใช้งานลูปเพื่อลดขนาดของทุกไฟล์ที่เลือก
    for file_path in file_paths:
        output_folder = os.path.join(os.path.dirname(file_path), 'min')

        # ถ้าไฟล์เป็น PNG ให้ทำการแปลงเป็น JPEG ก่อน
        if file_path.lower().endswith('.png'):
            file_path = convert_to_jpg(file_path, output_folder)
        
        # ตรวจสอบว่าได้รับไฟล์ JPEG หรือไม่
        if file_path and file_path.lower().endswith('.jpg'):
            reduce_image_size(file_path, output_folder, quality=60)

if __name__ == "__main__":
    select_files()
