require "cgi"

module SearchAliases
  def search_aliases(html, entries)
    text = CGI.unescapeHTML(html.to_s.gsub(/<(script|style)\b[^>]*>.*?<\/\1\s*>/mi, " ").gsub(/<[^>]*>/, " ")).gsub(/\s+/, " ")

    entries.flat_map do |entry|
      terms = [entry.fetch("acronym"), *entry.fetch("aliases")]
      present = terms.each_with_index.map do |term, index|
        pattern = Regexp.new("(?<![[:alnum:]])#{Regexp.escape(term)}(?![[:alnum:]])", index.zero? ? 0 : Regexp::IGNORECASE)
        text.match?(pattern)
      end
      present.any? ? terms.reject.with_index { |_, index| present[index] } : []
    end.join(" ")
  end
end

Liquid::Template.register_filter(SearchAliases)
