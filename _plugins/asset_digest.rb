# Content fingerprints for the static assets the markup loads.
#
# The HTML and those files are cached independently, so without a fingerprint a
# browser can pair new markup with the previous stylesheet until max-age
# expires and render a broken page. A digest changes only when the file does,
# so an unchanged asset keeps whatever the visitor already has.
require "digest"

ASSETS = [
  "style.css",
  "fonts/fonts.css",
  "js/lucide.min.js",
  "js/lottie.min.js",
  "js/marked.min.js",
].freeze

Jekyll::Hooks.register :site, :post_read do |site|
  site.data["asset_digests"] = ASSETS.to_h do |path|
    file = File.join(site.source, path)
    [path, File.file?(file) ? Digest::SHA256.file(file).hexdigest[0, 12] : ""]
  end
end