module Jekyll
    class ReplaceMdLinks < Generator
      priority :lowest
  
      def generate(site)
        site.pages.each do |page|
          if page.content
            # 替换 Markdown 链接中的 .md 为 .html
            page.content = page.content.gsub(/](\([^)]+)\.md\)/, "](\\1.html)")
          end
        end
  
        site.posts.docs.each do |post|
          if post.content
            # 替换 Markdown 链接中的 .md 为 .html
            post.content = post.content.gsub(/](\([^)]+)\.md\)/, "](\\1.html)")
          end
        end
      end
    end
  end
  