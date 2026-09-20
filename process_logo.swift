import Foundation
import CoreGraphics
import ImageIO

let inputURL = URL(fileURLWithPath: "/Users/thanhduy/Documents/olion-coffee/assets/logo.png")
guard let imageSource = CGImageSourceCreateWithURL(inputURL as CFURL, nil),
      let cgImage = CGImageSourceCreateImageAtIndex(imageSource, 0, nil) else {
    print("Failed to load image")
    exit(1)
}

let width = cgImage.width
let height = cgImage.height
let colorSpace = CGColorSpaceCreateDeviceRGB()
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * width
let rawData = UnsafeMutablePointer<UInt8>.allocate(capacity: height * bytesPerRow)

guard let context = CGContext(data: rawData,
                              width: width,
                              height: height,
                              bitsPerComponent: 8,
                              bytesPerRow: bytesPerRow,
                              space: colorSpace,
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue) else {
    print("Failed to create context")
    exit(1)
}

context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))

// Create transparent buffer and white buffer
let transData = UnsafeMutablePointer<UInt8>.allocate(capacity: height * bytesPerRow)
let whiteData = UnsafeMutablePointer<UInt8>.allocate(capacity: height * bytesPerRow)

for y in 0..<height {
    for x in 0..<width {
        let offset = (y * width + x) * 4
        let r = rawData[offset]
        let g = rawData[offset + 1]
        let b = rawData[offset + 2]
        let a = rawData[offset + 3]
        
        // Check if white background
        if r > 235 && g > 235 && b > 235 {
            transData[offset] = 0
            transData[offset + 1] = 0
            transData[offset + 2] = 0
            transData[offset + 3] = 0
            
            whiteData[offset] = 0
            whiteData[offset + 1] = 0
            whiteData[offset + 2] = 0
            whiteData[offset + 3] = 0
        } else {
            // Keep original colors for trans
            transData[offset] = r
            transData[offset + 1] = g
            transData[offset + 2] = b
            transData[offset + 3] = a
            
            // Invert/turn to warm white (#F6F1E7) for white version
            whiteData[offset] = 246
            whiteData[offset + 1] = 241
            whiteData[offset + 2] = 231
            whiteData[offset + 3] = a
        }
    }
}

func savePNG(data: UnsafeMutablePointer<UInt8>, path: String) {
    guard let ctx = CGContext(data: data, width: width, height: height, bitsPerComponent: 8, bytesPerRow: bytesPerRow, space: colorSpace, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue),
          let newImg = ctx.makeImage() else { return }
    let outURL = URL(fileURLWithPath: path) as CFURL
    guard let destination = CGImageDestinationCreateWithURL(outURL, "public.png" as CFString, 1, nil) else { return }
    CGImageDestinationAddImage(destination, newImg, nil)
    CGImageDestinationFinalize(destination)
}

savePNG(data: transData, path: "/Users/thanhduy/Documents/olion-coffee/assets/logo-trans.png")
savePNG(data: whiteData, path: "/Users/thanhduy/Documents/olion-coffee/assets/logo-white.png")
print("Processed logos successfully!")
