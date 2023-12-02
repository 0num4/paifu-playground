package code_rabbit_test

import "fmt"

type Person struct {
	Name string
}

func main() {
	fmt.Println("person.Name") // nilポインタの参照バグ
}
