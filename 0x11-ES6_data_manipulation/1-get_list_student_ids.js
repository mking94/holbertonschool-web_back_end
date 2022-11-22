export default function getListStudentIds(list) {
  let res = []
  if (typeof(list) === 'object') {
    for (i = 0; i < list.length; i++) {
      res.push(list[i].id);
    }
  }
  return res;
}
