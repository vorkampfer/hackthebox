package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"math/rand"
	"os/exec"
	"strconv"
	"strings"
)

func getSeed() (int64, string, error) {
	cmd := exec.Command(
		"curl",
		"-s", "-k", "-X", "GET",
		"https://user:DumpPassword$Here@127.0.0.1:9200/_search?pretty=true",
	)

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("Error: Command did not execute properly:", err)
		return 0, "", err
	}
	outputLines := strings.Split(string(output), "\n")
	var seedStr string

	for _, line := range outputLines {
		if strings.Contains(line, "seed") && !strings.Contains(line, "index") {
			seedStr = strings.TrimSpace(strings.Split(line, ":")[1])
			break
		}

	}
	seed, err := strconv.ParseInt(seedStr, 10, 64)
	if err != nil {
		fmt.Println("There was a problem in the data type conversion.:", err)
		return 0, "", err
	}

	var blob string

	for _, line := range outputLines {
		if strings.Contains(line, "blob") {
			line = strings.Split(line, ":")[1]
			blob = strings.Split(line, "\"")[1]
			break
		}
	}

	return seed, blob, err
}

func genKey(seed int64) []byte {
	rand.Seed(seed)
	key := make([]byte, 16)
	for i := 0; i < 16; i++ {
		key[i] = byte(rand.Intn(254) + 1)
	}
	return key
}
func decryptCFB(iv, ciphtertext, key []byte) []byte {
	block, _ := aes.NewCipher(key)

	plaintext := make([]byte, len(ciphtertext))
	stream := cipher.NewCFBDecrypter(block, iv)
	stream.XORKeyStream(plaintext, ciphtertext)
	return plaintext
}

func main() {
	seed, encryptedBlob, _ := getSeed()
	key := genKey(seed)
	decodedBlob, err := base64.URLEncoding.DecodeString(encryptedBlob)
	if err != nil {
		fmt.Println("Error in decryption process:", err)
		return
	}
	// fmt.Println(string(decodedBlob))
	iv := decodedBlob[:aes.BlockSize]
	encryptedData := decodedBlob[aes.BlockSize:]
	decryptedData := decryptCFB(iv, encryptedData, key)

	fmt.Println("The seed value is:", seed)
	fmt.Println("The blob value is:", encryptedBlob)
	fmt.Printf("The key is: %x\n", key)
	fmt.Println("The Decrytped pass phrase is:", string(decryptedData))
}
