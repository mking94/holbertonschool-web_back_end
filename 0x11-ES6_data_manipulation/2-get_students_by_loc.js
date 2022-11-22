export default function getListStudentIds(arrayobjects, loc) {
  if (!(Array.isArray(arrayobjects))) {
    return [];
  }
  return arrayobjects.filter(arrayobjects => arrayobjects.location == loc);
}
