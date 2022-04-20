let map=new Map();
map.set("Name", "Naga");      //add
map.set("Id", 34);
map.set("percentage", 89);
map.set("course","B.Tech");

console.log(map.get("Name"));    
console.log(map.has("subject"));          //search
console.log(map.size);          //length
map.delete("Id");
console.log(map);
//map.clear()      //clears the key-value pairs in map
map.forEach(display);
function display(value) {
    console.log(value);
}
for (let key of map.keys()) {
    console.log(key);
}


let fruits=["Mango","Apple","Orange","Banana"];
let set=new Set(fruits);
set.add("Strawberry");
console.log(set.delete("Apple"));
console.log(set);
console.log(set.has("Apple"));      //search
console.log(set.size);
//set.clear()    //clears the values in set

for (let value of set) {
    console.log(value);
}