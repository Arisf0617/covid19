package servlet;

import bean.China;
import com.google.gson.Gson;
import dao.ChinaMapper;
import org.apache.ibatis.session.SqlSession;
import util.MybatisUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

/**
 * @author MoooJL
 * @data 2020/9/30-19:41
 */
@WebServlet("/getAll")
public class getAll extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        SqlSession sqlSession = MybatisUtils.getSqlSession();
        ChinaMapper mapper = sqlSession.getMapper(ChinaMapper.class);
        List<China> list = mapper.getList();
        Gson gson = new Gson();
        String json = gson.toJson(list);
        System.out.println(json);
        response.setContentType("text/html;charset=utf-8");
        response.getWriter().write(json);
        sqlSession.close();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request,response);
    }
}
