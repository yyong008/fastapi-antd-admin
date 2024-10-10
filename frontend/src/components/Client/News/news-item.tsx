import { Link } from "@tanstack/react-router";
import { formatDate } from "@/utils/utils";

export function NewsItem(props: any) {
  const { data } = props;
  return (
    <div>
      <Link
        className="text-gray-900  hover:text-yellow-500"
        to={`/news/${props.data.id}`}
      >
        <div className="flex items-center">
          <h1 className="flex text-[16px] my-[10px]  before:block before:content-['·'] before:text-yellow-700 before:mr-[4px]">
            {data.title}
          </h1>
          <span className="flex items-center m-[10px] left-[10px] text-[14px] text-gray-400">
            {formatDate(data.created_at)}
          </span>
        </div>
      </Link>
    </div>
  );
}
