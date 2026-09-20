import Foundation
import CoreGraphics
import ImageIO

guard let imageSource = CGImageSourceCreateWithURL(URL(fileURLWithPath: "/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0/.user_uploaded/media_1789917213060.png") as CFURL, nil),
      let cgImage = CGImageSourceCreateImageAtIndex(imageSource, 0, nil) else {
    print("Failed to load image")
    exit(1)
}

let width = cgImage.width
let height = cgImage.height
print("Width: \(width), Height: \(height)")

// Helper function to save cropped image
func cropAndSave(x: CGFloat, y: CGFloat, w: CGFloat, h: CGFloat, filename: String) {
    let rect = CGRect(x: x, y: y, width: w, height: h)
    guard let cropped = cgImage.cropping(to: rect) else {
        print("Failed to crop \(filename)")
        return
    }
    let destURL = URL(fileURLWithPath: "/Users/thanhduy/Documents/olion-coffee/assets/menu/\(filename)") as CFURL
    guard let dest = CGImageDestinationCreateWithURL(destURL, "public.png" as CFString, 1, nil) else {
        print("Failed to create dest for \(filename)")
        return
    }
    CGImageDestinationAddImage(dest, cropped, nil)
    CGImageDestinationFinalize(dest)
    print("Saved \(filename) - Rect: \(rect)")
}

// Let's test a sample crop
cropAndSave(x: 18, y: 220, w: 90, h: 110, filename: "test_espresso.png")
