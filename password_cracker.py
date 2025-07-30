import hashlib
import itertools
import string


def generate_hashes(password_list):
    hashes = {}
    for password in password_list:
        hash_sha256 = hashlib.sha256(password.encode()).hexdigest()
        hashes[hash_sha256] = password
    return hashes


def brute_force(target_hash, max_length=4):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for length in range(1, max_length + 1):
        for candidate in itertools.product(chars, repeat=length):
            attempts += 1
            candidate = ''.join(candidate)
            candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
            if candidate_hash == target_hash:
                return candidate, attempts
    return None, attempts


if __name__ == "__main__":
    print("ARS Şifre Kırma Aracı")
    target_hash = input("Kırılacak SHA-256 hash'ini girin: ").strip()

    # Önce basit bir wordlist deneyelim
    common_passwords = ["password", "123456", "admin", "qwerty", "letmein"]
    hash_dict = generate_hashes(common_passwords)

    if target_hash in hash_dict:
        print(f"[+] Şifre bulundu: {hash_dict[target_hash]}")
    else:
        print("Wordlist'te bulunamadı. Brute-force başlatılıyor...")
        password, attempts = brute_force(target_hash, max_length=4)
        if password:
            print(f"[+] Şifre kırıldı: {password} (Deneme: {attempts})")
        else:
            print(f"[-] Şifre kırılamadı (Deneme: {attempts})")
