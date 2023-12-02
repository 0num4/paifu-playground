package code_rabbit_test

import "fmt"

type Person struct{}

func main() {
	fmt.Println("person.Name") // nilポインタの参照バグ
}
