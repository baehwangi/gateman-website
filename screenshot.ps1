Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Edge 브라우저 시작
$edge = Start-Process msedge -ArgumentList "--new-window", "file:///C:/Users/ASDS/Desktop/GATEMAN/index.html" -PassThru
Start-Sleep -Seconds 3

# 스크린샷 1: index.html
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap $bounds.Width, 300
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, [System.Drawing.Size]::new($bounds.Width, 300))
$bitmap.Save("C:\Users\ASDS\Desktop\GATEMAN\claudedocs\screenshot_index_header.png")
$graphics.Dispose()
$bitmap.Dispose()

Write-Host "Index header screenshot saved"

# 제품 페이지로 이동
Start-Process msedge -ArgumentList "--new-window", "file:///C:/Users/ASDS/Desktop/GATEMAN/products/gm-900s.html"
Start-Sleep -Seconds 3

# 스크린샷 2: 제품 페이지
$bitmap2 = New-Object System.Drawing.Bitmap $bounds.Width, 300
$graphics2 = [System.Drawing.Graphics]::FromImage($bitmap2)
$graphics2.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, [System.Drawing.Size]::new($bounds.Width, 300))
$bitmap2.Save("C:\Users\ASDS\Desktop\GATEMAN\claudedocs\screenshot_product_header.png")
$graphics2.Dispose()
$bitmap2.Dispose()

Write-Host "Product header screenshot saved"

# Edge 종료
Stop-Process -Name msedge -Force -ErrorAction SilentlyContinue
