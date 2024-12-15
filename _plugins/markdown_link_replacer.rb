# _plugins/replace_strings.rb

module Jekyll
  class ReplaceStringConverter < Converter
    # 设置转换器优先级，确保在 Markdown 转换之前执行替换
    # priority :low

    # 指定该转换器处理的文件扩展名
    def matches(ext)
      Jekyll.logger.debug "matches(ext): #{ext}"
      if ext != nil
        ext.downcase == '.md' || ext.downcase == '.markdown'
      end
      false
    end

    # 保持文件扩展名不变
    def output_ext(ext)
      Jekyll.logger.debug "output_ext(ext): #{ext}"
      ext
    end

    # 执行字符串替换并调用默认的 Markdown 转换器
    def convert(content)
      raise ThreadError
      Jekyll.logger.debug "Converting:", "111111111111"
      # 定义需要替换的字符串对，支持字符串和正则表达式
      replacements = [
        # { pattern: /\[([^\]]+)\]\(([^)]+)\.md\)/, replacement: '[\1](\2)' },
        # { pattern: /\[([^\]]+)\]\(([^)]+)\.md\)/, replacement: '[\1](\2)' },
#         { pattern: /旧字符串\d+/, replacement: '通用新字符串' }, # 使用正则表达式匹配“旧字符串”后跟一个或多个数字
        # 继续添加更多的替换规则
      ]

      # 进行字符串替换
      replacements.each do |rule|
        content = content.gsub(rule[:pattern], rule[:replacement])
      end

      # 使用默认的 Markdown 转换器处理替换后的内容
      ::Jekyll::Converters::Markdown.new.convert(content)
    end
  end
end
