import { Link } from "@tanstack/react-router";
import { formatDate } from "@/utils/utils";

export function BlogItem(props: any) {
  const { data } = props;
  return (
    <div>
      <Link className="hover:text-yellow-500" to={`/blog/${props.data.id}`}>
        <div className="flex items-center">
          <h1 className="flex text-[16px] my-[10px]  before:block before:content-['·'] before:text-yellow-700 before:mr-[4px]">
            {data.title}
          </h1>
          <span className="flex items-center m-[10px] left-[10px] text-[14px] text-gray-400">
            {formatDate(data.createdAt)}
          </span>
        </div>
      </Link>
    </div>
  );
}
