package main

import "fmt"

// Define an interface
type Shape interface {
    area() float64
}

// Define a struct
type Rectangle struct {
    width, height float64
}

// Rectangle implements Shape (automatically)
func (r Rectangle) area() float64 {
    return r.width * r.height
}
type Circle struct {
    radius float64
}

func (c Circle) area() float64 {
    return 3.14 * c.radius * c.radius
}

func printArea(s Shape) {
    fmt.Println("Area:", s.area())
}

func main() {
    r := Rectangle{width: 10, height: 5}
    c := Circle{radius: 3}
    printArea(r)
    printArea(c)
}
