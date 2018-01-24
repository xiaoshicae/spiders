class SumNineRegion:
    def conv(self, matrix, width, height, flag=1):
        converted = []
        for h in range(height):
            for w in range(width):
                # if matrix[h*width+w] == 1:
                #     converted.append(1)
                if h == 0:
                    if w == 0:
                        if matrix[h*width+w] + matrix[h*width+w+1] + matrix[(h+1)*width+w] + matrix[(h+1)*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    elif w == width - 1:
                        if matrix[h*width+w-1] + matrix[h*width+w] + matrix[(h+1)*width+w-1] + matrix[(h+1)*width+w] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    else:
                        if matrix[h*width+w-1] + matrix[h*width+w] + matrix[h*width+w+1] + matrix[(h+1)*width+w-1] + matrix[(h+1)*width+w] + matrix[(h+1)*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                elif h == height - 1:
                    if w == 0:
                        if matrix[(h-1)*width+w] + matrix[(h-1)*width+w+1] + matrix[h*width+w] + matrix[h*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    elif w == width - 1:
                        if matrix[(h-1)*width+w-1] + matrix[(h-1)*width+w] + matrix[h*width+w-1] + matrix[h*width+w] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    else:
                        if matrix[(h-1)*width+w-1] + matrix[(h-1)*width+w] + matrix[(h-1)*width+w+1] + matrix[h*width+w-1] + matrix[h*width+w] + matrix[h*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                else:
                    if w == 0:
                        if matrix[(h-1)*width+w] + matrix[(h-1)*width+w+1] + matrix[h*width+w] + matrix[h*width+w+1] + matrix[(h+1)*width+w] + matrix[(h+1)*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    elif w == width - 1:
                        if matrix[(h-1)*width+w-1] + matrix[(h-1)*width+w] + matrix[h*width+w-1] + matrix[h*width+w] + matrix[(h+1)*width+w-1] + matrix[(h+1)*width+w]> flag:
                            converted.append(1)
                        else:
                            converted.append(0)
                    else:
                        if matrix[(h-1)*width+w-1] + matrix[(h-1)*width+w] + matrix[(h-1)*width+w+1] + matrix[h*width+w-1] + matrix[h*width+w] + matrix[h*width+w+1] + matrix[(h+1)*width+w-1] + matrix[(h+1)*width+w] + matrix[(h+1)*width+w+1] > flag:
                            converted.append(1)
                        else:
                            converted.append(0)
        return converted

    def sum_9_region(self, img, x, y):
        """
        9邻域框,以当前点为中心的田字框,黑点个数
        :param x:
        :param y:
        :return:
        """
        # todo 判断图片的长宽度下限
        cur_pixel = img.getpixel((x, y))  # 当前像素点的值
        width = img.width
        height = img.height

        if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
            return 0

        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,3邻域
                sum = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
                return 4 - sum
            elif x == width - 1:  # 右上顶点,3邻域
                sum = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
                return 4 - sum
            else:  # 最上非顶点,5邻域
                sum = img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
                return 6 - sum
        elif y == height - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                sum = cur_pixel  + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x, y - 1))
                return 4 - sum
            elif x == width - 1:  # 右下顶点
                sum = cur_pixel + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y - 1))
                return 4 - sum
            else:  # 最下非顶点,6邻域
                sum = cur_pixel + img.getpixel((x - 1, y)) + img.getpixel((x + 1, y)) + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x + 1, y - 1))
                return 6 - sum
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
                return 6 - sum
            elif x == width - 1:  # 右边非顶点
                sum = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
                return 6 - sum
            else:  # 具备9领域条件的
                sum = img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
                return 9 - sum
