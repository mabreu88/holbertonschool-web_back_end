export default function getListStudents(StudentList) {
  if (!Array.isArray(StudentList)) return [];
  return StudentList.map((element) => element.id);
}
