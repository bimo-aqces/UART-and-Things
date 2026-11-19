import time
import keyboard
import serial

PORT = "COM3"  # Ganti jika port USB-to-TTL kamu bukan COM3
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.1)
time.sleep(1)
print(f"Terhubung ke {PORT} @ {BAUD}. Tekan SPASI untuk toggle LED (Ctrl+C keluar).")

try:
    while True:
        if keyboard.is_pressed("space"):
            ser.write(b" ")
            time.sleep(0.05)

        if ser.in_waiting > 0:
            balasan = ser.readline().decode(errors="ignore").strip()
            if balasan:
                print("STM32:", balasan)
except KeyboardInterrupt:
    print("\nSelesai.")
finally:
    ser.close()
