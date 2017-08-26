const containers = $('.col');
const nRows = [4, 2, 3, 5];
let index = 0;
let rowIndex = 0;
console.log('containers',containers);
while (index < containers.length) {
    const index2 = containers.length >= index + nRows[rowIndex] ? index + nRows[rowIndex] : containers.length;
    containers.slice(index, index2).wrapAll( "<div class='row' />");
    index = index2;
    rowIndex = rowIndex < nRows.length - 1 ? rowIndex + 1 : 0;
}
