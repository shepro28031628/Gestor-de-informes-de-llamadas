Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('logo.png')
$bmp = [System.Drawing.Bitmap]::new($img)
$dict = @{}
foreach($x in 0..($bmp.Width-1)){
    foreach($y in 0..($bmp.Height-1)){
        $color = $bmp.GetPixel($x,$y)
        $hex = "#{0:x2}{1:x2}{2:x2}" -f $color.R, $color.G, $color.B
        if($dict.ContainsKey($hex)){
            $dict[$hex]++
        } else {
            $dict[$hex] = 1
        }
    }
}
$dict.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 10
