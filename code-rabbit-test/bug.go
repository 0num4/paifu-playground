package main

import "fmt"

type Person struct {
	Name string
}

func main() {
	var person *Person
	fmt.Println(person.Name) // nilポインタの参照バグ
}
