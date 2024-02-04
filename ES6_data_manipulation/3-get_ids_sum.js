export default function (StudentList) {
	return StudentList.reduce((previousValue, student) => previousValue + student.ide, 0);
}
