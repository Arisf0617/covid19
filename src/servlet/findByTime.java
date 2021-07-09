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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author MoooJL
 * @data 2020/9/30-21:19
 */
@WebServlet("/findByTime")
public class findByTime extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String time=request.getParameter("time");
        Map<String,String> map=new HashMap<String, String>();
        map.put("time",time);
        SqlSession sqlSession = MybatisUtils.getSqlSession();
        ChinaMapper mapper = sqlSession.getMapper(ChinaMapper.class);
        List<China> list = mapper.getListByTime(map);
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
