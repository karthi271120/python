export function calculateTotalMarks(...marks) {
  return marks.reduce((total, mark) => total + mark, 0);
}

export function welcomeUser(name = "Guest") {
  return `Welcome ${name}`;
}