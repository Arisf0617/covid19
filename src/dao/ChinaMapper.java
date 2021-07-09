package dao;

import bean.China;

import java.util.List;
import java.util.Map;

/**
 * @author MoooJL
 * @data 2020/9/30-18:44
 */
public interface ChinaMapper {
    List<China> getListByTime(Map<String, String> map);
    List<China> getList();
    List<China> getListByBETime(Map<String, String> map);
}
