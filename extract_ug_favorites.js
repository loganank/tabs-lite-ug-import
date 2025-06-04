const tabData = Array.from(document.querySelectorAll('a'))
    .filter(a => a.href.includes('/tab/'))
    .map(a => ({
        title: a.textContent.trim(),
        url: a.href
    }))
    .filter(tab => tab.title);

console.table(tabData);

// Create CSV content
const csvContent = 'Title,URL\n' + tabData
  .map(row => `"${row.title.replace(/"/g, '""')}","${row.url}"`)
  .join('\n');

// Create a blob and download it
const blob = new Blob([csvContent], { type: 'text/csv' });
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'tabs.csv';
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
URL.revokeObjectURL(url);
