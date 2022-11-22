export default function getListStudentIds(arrayobjects, city) {
  if (!(Array.isArray(arrayobjects))) {
    return [];
  }
  return arrayobjects.filter((value) => value.location === city);
}
