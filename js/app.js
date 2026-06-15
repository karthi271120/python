// app.js

import { students } from "./student.js";
import { calculateTotalMarks, welcomeUser } from "./utils.js";


const names = students.map(student => console.log(student.skills));

console.log(calculateTotalMarks(35, 40, 50, 34))
console.log(welcomeUser('yuva'))
console.log()





